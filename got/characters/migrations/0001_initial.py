# Generated by Django 2.0.4 on 2018-04-07 18:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('places', '0001_initial'),
        ('seasons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('is_alive', models.BooleanField(default=False)),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='places.Place')),
                ('seasons', models.ManyToManyField(to='seasons.Season')),
            ],
        ),
    ]
