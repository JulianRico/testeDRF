from .models import Report
from rest_framework import viewsets, permissions
from .serializers import ReportSerializer
from .permissions import IsAuthenticatedByJWT


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    permission_classes = [IsAuthenticatedByJWT]
    serializer_class = ReportSerializer
