# coding: utf-8

from rest_framework import serializers

from .models import Raspberry_pi


class Raspberry_piSerializer(serializers.ModelSerializer):
  class Meta:
   model = Raspberry_pi
   #fields = ('IP_address', 'Host_name', 'MAC_address',) # 追加要素アリ
   fields = '__all__'
