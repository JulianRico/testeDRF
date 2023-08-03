from companies.serializers import UserCompanySerializer
from companies.models import Companie
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
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


class UserCompanyCreateView(CreateAPIView):
    serializer_class = UserCompanySerializer

    def create(self, request, *args, **kwargs):
        # Obtener el ID de la compañía de la URL
        companie_id = self.kwargs.get('companie_id')
        print(companie_id)
        try:
            companie = Companie.objects.get(pk=companie_id)
            print(companie)
        except Companie.DoesNotExist:
            return Response({"error": "Companie not found"}, status=status.HTTP_404_NOT_FOUND)

        # Agregar el ID de la compañía a los datos
        request.data['companie'] = companie.id
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
