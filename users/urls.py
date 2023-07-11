from django.urls import path
from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()

router = routers.DefaultRouter()
router.register('api/users', UserViewSet, basename='users')

urlpatterns = [
    path(r'api/users/<str:name>/',
         UserViewSet.as_view({'get': 'retrieve_by_name'}), name='retrieve_by_name_user'),
    *router.urls,
]
