# Generated by Django 2.1.2 on 2018-12-14 07:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_raspberry_pi_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='author',
        ),
        migrations.AlterField(
            model_name='raspberry_pi',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 14, 7, 56, 7, 237314)),
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
