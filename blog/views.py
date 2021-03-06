
# coding: utf-8


import django_filters
from rest_framework import viewsets, filters

from .models import Raspberry_pi
from .serializer import  Raspberry_piSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

#
from rest_framework import generics
#


#
from django.http import HttpResponse
import os
from django.conf import settings
#

from rest_framework.decorators import api_view



class FileGet(APIView):
 def get(self, request, format=None):
  #file_path = os.path.join(settings.MEDIA_ROOT, "5.jpeg")
  file_path = os.path.join(settings.MEDIA_ROOT, "test.txt")
  FilePointer = open(file_path,"rb")
  response = HttpResponse(FilePointer,content_type='application/msword')
  #response = HttpResponse(FilePointer,content_type='image/jpeg')
  response['Content-Disposition'] = 'filename=test.txt'

  return response

 #return Response("file download")


class Raspberry_piViewSet(viewsets.ModelViewSet):
    queryset = Raspberry_pi.objects.all()
    serializer_class = Raspberry_piSerializer
    filter_fields = ('id', 'MAC_address', 'IP_address', 'Host_name', 'Date')
  #  @action


#class Raspberry_piViewSet(generics.ListCreateAPIView):
#    queryset = Raspberry_pi.objects.all()
#    serializer_class = Raspberry_piSerializer
#    filter_fields = ('MAC_address', 'IP_address', 'Host_name', 'Date')

