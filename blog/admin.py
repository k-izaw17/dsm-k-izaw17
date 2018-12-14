from django.contrib import admin

# Register your models here.
from .models import Raspberry_pi


@admin.register(Raspberry_pi)
class Raspberry_pi(admin.ModelAdmin):
    pass

