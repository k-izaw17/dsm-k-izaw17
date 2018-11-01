# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import User, Entry, Raspberry_pi
from .serializer import UserSerializer, EntrySerializer, Raspberry_piSerializer

from rest_framework.views import APIView
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class TaskGet(APIView):
    def get(self, request, format=None):
        return Response("hallo")

class Raspberry_piViewSet(viewsets.ModelViewSet):
    queryset = Raspberry_pi.objects.all()
    serializer_class = Raspberry_piSerializer
