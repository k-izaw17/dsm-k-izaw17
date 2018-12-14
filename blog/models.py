from datetime import datetime
from django.db import models
from django.utils.timezone import now


class Raspberry_pi(models.Model):
  #id = AutoField()
  MAC_address = models.CharField(max_length=128)
  IP_address = models.GenericIPAddressField(default='127.0.0.1')
  Host_name = models.CharField(max_length=128, default='TEST')
  Date = models.DateTimeField(default=datetime.utcnow())


