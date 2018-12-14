
# coding: utf-8

import django_filters
from rest_framework import viewsets, filters

from .models import Raspberry_pi
from .serializer import  Raspberry_piSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

#FILE
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework_files.viewsets import ImportExportModelViewSet

#
from django.http import HttpResponse
import io
import xlwt
import os
from django.conf import settings


#



class FileGet(APIView):
# def get(self, request, format=None):
# return Response("hallo")
 def get(self, request, format=None):
     output = io.BytesIO()
     #
     wb = xlwt.Workbook()
     ws = wb.add_sheet("sheet 1")

     for i in range(100):
        ws.write(i//10, i%10, i)
     wb.save(output)
    #
     response = HttpResponse(output.getvalue(), content_type="application/excel")
     response["Content-Disposition"] = "filename=text1.xls"
     return response


# def get(self, request, path, format=None):
 #   file_path = os.path.join(settings.MEDIA_ROOT, path)
  #  if os.path.exists(file_path):
   #     with open(file_path, 'rb') as fh:
     #       response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
    #        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
      #      return response
    

class Raspberry_piViewSet(viewsets.ModelViewSet):
    queryset = Raspberry_pi.objects.all()
    serializer_class = Raspberry_piSerializer




