import io
import os
from django.http import FileResponse, HttpResponse
from django.views import View
from .report_pdf_estacionario import GeneratePDFintoSVG
from .models import Report
from datetime import datetime
from users.models import User
from companies.models import Companie, UserCompany
import pdfkit
import platform
import tempfile
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives


class SVGtoPDFView(View):
    def get(self, request, *args, **kwargs):
        id_from_url = kwargs.get('id_report')

        print(id_from_url)

        try:
            # Consulta el modelo Report usando el ID
            report = Report.objects.get(id=id_from_url)
        except Report.DoesNotExist:
            return HttpResponse("El reporte no existe.")

        # Aquí puedes acceder a los campos del reporte
        # Convierte la cadena de fecha a un objeto datetime
        fecha = report.create_at
        fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S.%f%z")
        fechafull = fecha_str.split(" ")
        fecha_objeto = datetime.strptime(fechafull[0], "%Y-%m-%d")
        fecha_convertida = fecha_objeto.strftime("%d-%m-%Y")

        questions_mtto = report.questionsmtto
        question_views = report.questionviews
        questions_deterioration = report.questionsdeterioration
        tank_identification = report.tankidentification
        observations_and_results = report.observationsandresults
        signatures = report.signatures
        photos = report.photos

        try:
            # Consulta el modelo Report usando el ID
            user = User.objects.get(name=report.user)
        except User.DoesNotExist:
            return HttpResponse("El usuario no existe.")
        print(user.email)

        try:
            # Consulta el modelo Report usando el ID
            companie = Companie.objects.get(name=report.companie)
        except Companie.DoesNotExist:
            return HttpResponse("la compañia no existe.")
        print(companie.email)

        try:
            # Consulta el modelo Report usando el ID
            companieuser = UserCompany.objects.get(usuario=report.userCompany)
        except UserCompany.DoesNotExist:
            return HttpResponse("El usuario de compañia no existe.")
        print(companieuser)

        # Pasa los campos a la función GeneratePDFintoSVG
        svg_code = GeneratePDFintoSVG(
            questions_mtto, question_views, questions_deterioration, tank_identification,
            observations_and_results, signatures, photos, fecha_convertida, companieuser, companie, user, id_from_url
        )

        pdf_buffer = self.convert_svg_to_pdf(svg_code)

        # Envía el PDF por correo electrónico
        # self.send_email_with_attachment(id_from_url, companie.name,
        #           companie.email, companieuser.emailContact, user.email, fecha_convertida)
        response = HttpResponse(
            pdf_buffer["bufer"], content_type='application/pdf')
        # response = FileResponse(open(pdf_buffer, 'rb'), as_attachment=True)
        response['Content-Disposition'] = f'attachment; filename="ReporteQ-Checker_{id_from_url}.pdf"'

        os.remove(pdf_buffer["path"])
        return response

    def convert_svg_to_pdf(self, svg_code):

        try:
            svg_height = "14in"
            # Configura las opciones de pdfkit
            options = {
                'page-size': 'A4',
                'margin-top': '7mm',
                'margin-right': '20mm',
                'margin-bottom': '0mm',
                'margin-left': '20mm',
                'encoding': "UTF-8",
                'no-outline': None,
                'dpi': 999,
                'zoom': '1',
                'viewport-size': f'x{svg_height}',
                'image-dpi': 900
            }

            temp_svg_path = tempfile.NamedTemporaryFile(
                delete=False, suffix=".svg")
            temp_svg_path.write(svg_code.encode())
            temp_svg_path.close()

            temp_pdf_path = tempfile.NamedTemporaryFile(
                delete=False, suffix=".pdf")
            if platform.system() == 'Windows':

                config = pdfkit.configuration(
                    wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')

            # Genera el PDF desde el contenido SVG
                pdfkit.from_file(temp_svg_path.name, temp_svg_path.name + '.pdf',
                                 options=options, configuration=config)

            else:
                # Genera el PDF desde el contenido SVG
                pdfkit.from_file(temp_svg_path.name, temp_svg_path.name + '.pdf',
                                 options=options)
            with open(temp_svg_path.name + '.pdf', 'rb') as pdf_file:
                pdf_buffer = io.BytesIO(pdf_file.read())
                # Eliminar los archivos temporales
            os.remove(temp_svg_path.name)
            os.remove(temp_svg_path.name + '.pdf')
            print("PDF generado exitosamente en:", temp_pdf_path.name)

            return {'bufer': pdf_buffer, 'path': temp_pdf_path.name}

        except Exception as e:
            print("Error al generar el PDF:", str(e))


# Create your views here.


class SetSatus(View):
    def get(self, request, *args, **kwargs):
        try:
            report_id = kwargs.get('report_id')
            print(report_id)
            new_status = 3
            report = Report.objects.get(pk=report_id)
            print(report.status)
            report.status = new_status
            report.save()

            fecha = report.create_at
            fecha_str = fecha.strftime("%Y-%m-%d %H:%M:%S.%f%z")
            fechafull = fecha_str.split(" ")
            fecha_objeto = datetime.strptime(fechafull[0], "%Y-%m-%d")
            fecha_convertida = fecha_objeto.strftime("%d-%m-%Y")

            try:
                # Consulta el modelo Report usando el ID
                user = User.objects.get(name=report.user)
            except User.DoesNotExist:
                return HttpResponse("El usuario no existe.")
            print(user.email)

            try:
                # Consulta el modelo Report usando el ID
                companie = Companie.objects.get(name=report.companie)
            except Companie.DoesNotExist:
                return HttpResponse("la compañia no existe.")
            print(companie.email)

            try:
                # Consulta el modelo Report usando el ID
                companieuser = UserCompany.objects.get(
                    usuario=report.userCompany)
            except UserCompany.DoesNotExist:
                return HttpResponse("El usuario de compañia no existe.")
            print(companieuser)

            self.send_email_with_attachment(
                report_id, fecha_convertida, companie.email, user.email, companieuser.emailContact, companie.name)
            return HttpResponse(f"Reporte aprobado {report_id}.")
        except Report.DoesNotExist:
            return HttpResponse(f"El reporte {report_id} no Existe.")

    def send_email_with_attachment(self, id, fecha, correoempresa, correousuario, correousuarioempresa, namecompanie):

        # Reemplaza con la URL real
        url_descargar = f'https://api-qc-drf.onrender.com/api/pdfcreate/{id}'

        subject = 'Entrega de Reporte Q-Checker S.A.S'
        from_email = 'julianrico@outlook.com'
        to = [correoempresa, correousuario, correousuarioempresa]
        # Genera el contenido HTML directamente en el código
        html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Reporte Q-Checker S.A.S</title>
    </head>
    <body>
        <p>Estimado(a) {namecompanie},</p>        
        <p>Por favor, descarga el Reporte {id} : {fecha}</p>

        <div style="margin-top: 20px;">            
            <a href="{url_descargar}" style="background-color: #008CBA; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px; margin-left: 10px;">Descargar</a>
        </div>

        <p>Mensaje enviado por el sistema de reportes.</p>
        <p>No contestar este mensaje,</p>
        <p>Estamos comprometidos con el medio Ambiente, por favor no imprimir este documento si no es necesario, Politica de Cero Papel - Q-Checker S.A.S</p>        
    </body>
    </html>
    """

        # Elimina las etiquetas HTML para el contenido de texto
        text_content = strip_tags(html_content)

        # Agrega el archivo PDF adjunto
        email = EmailMultiAlternatives(subject, text_content, from_email, to)

        # Agrega el contenido HTML como alternativa
        email.attach_alternative(html_content, "text/html")
        # Envía el correo electrónico
        email.send()
        # se borrar el archivo pdf
