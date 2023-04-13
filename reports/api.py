from .models import Report
from rest_framework import viewsets, permissions
from .serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    permission_classes = [permissions.AllowAny]    
    serializer_class = ReportSerializer
    