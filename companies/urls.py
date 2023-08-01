from rest_framework import routers

from .api import CompanieViewSet, UserCompanieViewSet

router = routers.DefaultRouter()

router.register('api/companies', CompanieViewSet, 'companies')
router.register('api/usercompanies', UserCompanieViewSet, 'usercompanies')
urlpatterns = router.urls
