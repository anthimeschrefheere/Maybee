# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('adresse', models.CharField(max_length=250)),
                ('nb_kilo_miel', models.FloatField()),
                ('nb_ruches', models.IntegerField()),
                ('type_miel', models.CharField(max_length=50)),
                ('evolution_population', models.FloatField()),
                ('facteurs', models.CharField(max_length=50, choices=[(b'a', b'Frelon asiatique'), (b'b', b'Gel printanier'), (b'c', b'printemps pr\xc3\xa9coce'), (b'd', b'pesticides'), (b'e', b'OGM proches')])),
            ],
        ),
        migrations.CreateModel(
            name='profil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profil_nom', models.CharField(max_length=255)),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
