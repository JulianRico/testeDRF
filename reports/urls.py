from rest_framework import routers
from .api import ReportViewSet

router = routers.DefaultRouter()

router.register('api/reports', ReportViewSet,'reports')

urlpatterns = router.urls