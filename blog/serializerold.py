# coding: utf-8

from rest_framework import serializers

from .models import User, Entry, Raspberry_pi


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')



class EntrySerializer(serializers.ModelSerializer):
    # authorのserializerを上書き
    author = UserSerializer()

    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')

class Raspberry_piSerializer(serializers.ModelSerializer):
  class Meta:
   model = Raspberry_pi
   #fields = ('IP_address', 'Host_name', 'MAC_address',) # 追加要素アリ
   fields = '__all__'
