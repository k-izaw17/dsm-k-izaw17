# coding: utf-8

from rest_framework import routers
from .views import UserViewSet, EntryViewSet, Raspberry_piViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'Raspberry_pies', Raspberry_piViewSet)
