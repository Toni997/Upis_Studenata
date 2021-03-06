# Generated by Django 4.0.4 on 2022-06-03 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=255)),
                ('kod', models.CharField(max_length=16)),
                ('program', models.TextField()),
                ('bodovi', models.IntegerField()),
                ('sem_redovni', models.IntegerField()),
                ('sem_izvanredni', models.IntegerField()),
                ('izborni', models.CharField(choices=[('da', 'Da'), ('ne', 'Ne')], default='ne', max_length=10)),
                ('nositelj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
