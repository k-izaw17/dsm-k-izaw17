# Generated by Django 2.1.2 on 2018-10-30 08:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_raspberry_pi'),
    ]

    operations = [
        migrations.AddField(
            model_name='raspberry_pi',
            name='Host_name',
            field=models.CharField(default='TEST', max_length=128),
        ),
        migrations.AddField(
            model_name='raspberry_pi',
            name='IP_address',
            field=models.GenericIPAddressField(default='127.0.0.1'),
        ),
        migrations.AlterField(
            model_name='raspberry_pi',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
