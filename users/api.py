import statistics
from rest_framework.response import Response
from .models import User
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, status
from .serializers import UserSerializer
from .permissions import IsAuthenticatedByJWT


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedByJWT]
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], url_path='(?P<name>[^/.]+)')
    def retrieve_by_name(self, request, name=None):
        print(name)
        print('Ingresó a la función')
        user = self.queryset.filter(name=name).first()

        if user is None:
            return Response({'error': 'No se encontró ningún usuario con ese nombre'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
