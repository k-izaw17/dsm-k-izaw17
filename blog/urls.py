# coding: utf-8

from rest_framework import routers
from .views import Raspberry_piViewSet


router = routers.DefaultRouter()
#router = routers.ImportExportRouter()
router.register(r'Raspberry_pies', Raspberry_piViewSet)

#urlpatterns = router.urls
