from django.shortcuts import render
import io
from django.http import FileResponse, HttpResponse
from django.views import View
from django.core.mail import EmailMessage, get_connection
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from .report_pdf_estacionario import GeneratePDFintoSVG
from .models import Report
from datetime import datetime
from users.models import User
from companies.models import Companie, UserCompany


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

        print(report.userCompany)
        print(report.companie)
        print(report.user)

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
        print(companieuser.emailContact)

        # Pasa los campos a la función GeneratePDFintoSVG
        svg_code = GeneratePDFintoSVG(
            questions_mtto, question_views, questions_deterioration, tank_identification,
            observations_and_results, signatures, photos, fecha_convertida
        )

        pdf_buffer = self.convert_svg_to_pdf(svg_code)

        # Envía el PDF por correo electrónico
        self.send_email_with_attachment(pdf_buffer, id_from_url, companie.name,
                                        companie.email, companieuser.emailContact, user.email, fecha_convertida)

        return HttpResponse("Correo enviado con el PDF adjunto")

    def convert_svg_to_pdf(self, svg_code):
        buffer = io.BytesIO()
        drawing = svg2rlg(io.StringIO(svg_code))
        renderPDF.drawToFile(drawing, buffer)
        buffer.seek(0)
        return buffer

    def send_email_with_attachment(self, pdf_buffer, id, namecompanie, correoempresa, correousuario, correousuarioempresa, fecha):
        email = EmailMessage(
            subject='Reporte Quality Checker',
            body=f'Adjunto el reporte para la empresa {namecompanie} Generado el dia: {fecha}.',
            from_email='julianrico@outlook.com',
            to=[correoempresa, correousuario, correousuarioempresa],

        )
        nombrefichero = namecompanie + "_" + str(id) + ".pdf"
        # Agrega el archivo PDF adjunto
        email.attach(nombrefichero,
                     pdf_buffer.read(), 'application/pdf')

        # Envía el correo electrónico
        email.send()
# Create your views here.
