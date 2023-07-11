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

    @action(detail=True, methods=['delete'])
    def delete(self, request,  *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'error': 'usuario eliminado'}, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['put'])
    def put(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'], url_path='(?P<name>[^/.]+)')
    def retrieve_by_name(self, request, name=None, *args, **kwargs):
        print(name)
        print('Ingresó a la función')
        user = self.queryset.filter(name=name).first()
        if user is None:
            return Response({'error': 'No se encontró ningún usuario con ese nombre'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
