from .models import Companie
from rest_framework import viewsets, permissions
from .serializers import CompanieSerializer
from .permissions import IsAuthenticatedByJWT


class CompanieViewSet(viewsets.ModelViewSet):
    queryset = Companie.objects.all()
    permission_classes = [IsAuthenticatedByJWT]
    serializer_class = CompanieSerializer
