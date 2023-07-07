from rest_framework.response import Response
from .models import User
from rest_framework.decorators import action
from rest_framework import viewsets,  status
from .serializers import UserSerializer
from .permissions import IsAuthenticatedByJWT


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedByJWT]
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'], url_path='(?P<name>[^/.]+)')
    def retrieve_by_name(self, name=None):
        user = self.queryset.filter(name=name).first()

        if user is None:
            return Response({'error': 'No se encontró ningún usuario con ese nombre'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['put'], url_path='(?P<id>[^/.]+)')
    def put(self, request, id=None, *args, **kwargs):
        print(id)
        instance = self.queryset.filter(id=id).first()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=['delete'], url_path='(?P<idDelete>[^/.]+)')
    def delete(self, request, idDelete=None, *args, **kwargs):
        instance = self.queryset.filter(id=idDelete).first()
        instance.delete()
        print(instance)
        return Response({'msj': 'Usuario ${instance}'}, status=status.HTTP_204_NO_CONTENT)
