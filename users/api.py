from .models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer
from .permissions import IsAuthenticatedByJWT


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedByJWT]
    serializer_class = UserSerializer
