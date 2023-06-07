from rest_framework import routers

from .api import CompanieViewSet

router = routers.DefaultRouter()

router.register('api/companies', CompanieViewSet, 'companies')

urlpatterns = router.urls
