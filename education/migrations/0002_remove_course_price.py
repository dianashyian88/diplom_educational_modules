# Generated by Django 4.2.9 on 2024-01-29 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
    ]