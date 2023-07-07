from django.urls import path
from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()

router = routers.DefaultRouter()
router.register('api/user', UserViewSet, basename='users')

urlpatterns = [
    *router.urls,
    path('api/user/<str:name>/',
         UserViewSet.as_view({'get': 'retrieve_by_name'}), name='retrieve_by_name'),
]
