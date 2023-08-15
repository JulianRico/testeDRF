from rest_framework import serializers
from .models import Report
from users.models import User
from companies.models import Companie, UserCompany
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name',)


class CompanieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companie
        fields = ('name',)


class UserCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCompany
        fields = ('usuario',)


class ReportSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    companie = CompanieSerializer()
    status_display = serializers.SerializerMethodField()
    userCompany = UserCompanySerializer()

    class Meta:
        model = Report
        fields = ('id', 'status_display', 'status', 'questionsmtto', 'questionviews', 'tankidentification', 'observationsandresults', 'signatures',
                  'questionsdeterioration', 'photos', 'user', 'companie', 'userCompany', 'create_at')
        read_only_fields = ('create_at', 'id')

    def get_status_display(self, obj):
        return dict(Report.SelfStatus).get(obj.status)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        companie_data = validated_data.pop('companie')
        user_company_data = validated_data.pop('userCompany')

        user, _ = User.objects.get_or_create(**user_data)
        companie, _ = Companie.objects.get_or_create(**companie_data)
        user_company, _ = UserCompany.objects.get_or_create(
            **user_company_data)

        report = Report.objects.create(
            user=user,
            companie=companie,
            userCompany=user_company,
            **validated_data
        )

        print(report)
        self.send_email(report.id)
        return report

    def send_email(self, id):
        # Reemplaza con la URL real
        url_revisar = f'http://127.0.0.1:8000/api/pdfcreate/{id}'
        # Reemplaza con la URL real
        url_aprobar = f'http://127.0.0.1:8000/api/pdfcreate/{id}'

        subject = 'Informe para su revisión y aprobación'
        from_email = 'julianrico@outlook.com'
        to = ['juliquinterorico@hotmail.com', 'dddinamico@gmail.com']
        # Genera el contenido HTML directamente en el código
        html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Informe para Revisión y Aprobación</title>
    </head>
    <body>
        <p>Estimado(a) destinatario,</p>
        <p>Adjunto encontrarás un informe que requiere tu revisión y aprobación.</p>
        <p>Por favor, toma un momento para revisar el informe {id} y realizar la acción correspondiente:</p>

        <div style="margin-top: 20px;">
            <a href="{url_revisar}" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px;">Revisar</a>
            <a href="{url_aprobar}" style="background-color: #008CBA; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; border-radius: 5px; margin-left: 10px;">Aprobar</a>
        </div>

        <p>Mensaje enviado por el sistema de reportes.</p>
        <p>No contestar este mensaje,</p>        
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
