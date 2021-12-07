# Generated by Django 3.1.4 on 2021-07-25 23:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Organ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organ_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('quantity', models.IntegerField(default=1, null=True)),
                ('hospital_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('hospital_address', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('hospital_phone', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('date', models.DateField(default=datetime.datetime.today, null=True)),
                ('donar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donar.donar')),
            ],
        ),
    ]
