from django.urls import path
from rest_framework import routers
from .api import ReportViewSet
from .views import SVGtoPDFView, SetSatus

router = routers.DefaultRouter()

router.register(r'api/reports', ReportViewSet, 'reports')

urlpatterns = [
    path(r'api/pdfcreate/<int:id_report>/',
         SVGtoPDFView.as_view(), name='ReportePDF'),
    path(r'api/reportaprobe/<int:report_id>/',
         SetSatus.as_view(), name='AprbarReporte'),
    *router.urls
]
