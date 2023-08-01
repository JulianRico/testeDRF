from .models import Companie, UserCompany
from rest_framework import viewsets, permissions
from .serializers import CompanieSerializer, UserCompanySerializer
from .permissions import IsAuthenticatedByJWT


class CompanieViewSet(viewsets.ModelViewSet):
    queryset = Companie.objects.all()
    permission_classes = [IsAuthenticatedByJWT]
    serializer_class = CompanieSerializer


class UserCompanieViewSet(viewsets.ModelViewSet):
    queryset = UserCompany.objects.all()
    permission_classes = [IsAuthenticatedByJWT]
    serializer_class = UserCompanySerializer
