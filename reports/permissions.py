from rest_framework.permissions import BasePermission
from django.conf import settings
import jwt


class IsAuthenticatedByJWT(BasePermission):
    def has_permission(self, request, view):
        print(request.META.get('HTTP_AUTHORIZATION', '').split(' '))
        token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')
        if token == ['']:
            return False
        try:
            token = request.META.get('HTTP_AUTHORIZATION', '').split(' ')[1]
            jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.exceptions.InvalidTokenError:
            return False

        return True
