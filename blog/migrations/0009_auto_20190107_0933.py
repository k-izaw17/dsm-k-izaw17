# Generated by Django 2.1.2 on 2019-01-07 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20181226_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raspberry_pi',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 7, 9, 33, 13, 443035)),
        ),
    ]
