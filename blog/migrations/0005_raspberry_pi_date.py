# Generated by Django 2.1.2 on 2018-11-29 11:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181030_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='raspberry_pi',
            name='Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
