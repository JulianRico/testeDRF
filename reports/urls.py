from django.urls import path
from rest_framework import routers
from .api import ReportViewSet
from .views import SetSatus, SVGtoPdfImagesView,  CertificatePDFView, SetStatusReject

router = routers.DefaultRouter()

router.register(r'api/reports', ReportViewSet, 'reports')

urlpatterns = [
     path(r'api/reportreject/<int:id_report>/',
         SetStatusReject.as_view(), name='SetStatusReject'),
     path(r'api/pdfcreateimages/<int:id_report>/',
         SVGtoPdfImagesView.as_view(), name='ReporteImagenesPDF'),
     path(r'api/pdfcreatecertificate/<int:id_report>/',
         CertificatePDFView.as_view(), name='CertificadosPDF'),
     path(r'api/reportaprobe/<int:report_id>/',
         SetSatus.as_view(), name='AprobarReporte'),
    *router.urls
]
