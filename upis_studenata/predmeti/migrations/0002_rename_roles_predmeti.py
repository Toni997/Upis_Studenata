# Generated by Django 4.0.4 on 2022-06-03 00:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('predmeti', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Roles',
            new_name='Predmeti',
        ),
    ]
