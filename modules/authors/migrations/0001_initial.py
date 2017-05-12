# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-12 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=50)),
                ('biografia', models.TextField(blank=True, null=True)),
                ('sexo', models.CharField(choices=[('M', 'Mujer'), ('H', 'Hombre')], max_length=16)),
                ('genero_literario', models.CharField(choices=[('CM', 'Comedia'), ('TR', 'Terror'), ('DR', 'Drama')], max_length=100)),
                ('edad', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
