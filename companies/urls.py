from django.urls import path
from rest_framework import routers

from .api import CompanieViewSet, UserCompanieViewSet, UserCompanyCreateView

router = routers.DefaultRouter()

router.register('api/companies', CompanieViewSet, 'companies')
router.register('api/usercompanies', UserCompanieViewSet, 'usercompanies')

urlpatterns = [
    *router.urls,
    path(r'api/userCompany/<int:companie_id>/add/',
         UserCompanyCreateView.as_view(), name='add-user-company')

]
