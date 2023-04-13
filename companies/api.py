from .models import Companie
from rest_framework import viewsets, permissions
from .serializers import CompanieSerializer


class CompanieViewSet(viewsets.ModelViewSet):
    queryset = Companie.objects.all()
    permission_classes = [permissions.AllowAny]    
    serializer_class = CompanieSerializer
    