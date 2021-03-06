# Generated by Django 2.2 on 2020-09-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('surname', models.CharField(blank=True, max_length=30)),
                ('fathername', models.CharField(blank=True, max_length=30)),
                ('birth_year', models.PositiveIntegerField(blank=True)),
                ('death_year', models.PositiveIntegerField(blank=True)),
                ('place1_x', models.FloatField(blank=True)),
                ('place1_width', models.FloatField(blank=True)),
                ('place1_y', models.FloatField(blank=True)),
                ('place1_heigth', models.FloatField(blank=True)),
                ('place1_start_year', models.PositiveIntegerField(blank=True)),
                ('place1_end_year', models.PositiveIntegerField(blank=True)),
                ('place2_x', models.FloatField(blank=True)),
                ('place2_width', models.FloatField(blank=True)),
                ('place2_y', models.FloatField(blank=True)),
                ('place2_heigth', models.FloatField(blank=True)),
                ('place2_start_year', models.PositiveIntegerField(blank=True)),
                ('place2_end_year', models.PositiveIntegerField(blank=True)),
                ('place3_x', models.FloatField(blank=True)),
                ('place3_width', models.FloatField(blank=True)),
                ('place3_y', models.FloatField(blank=True)),
                ('place3_heigth', models.FloatField(blank=True)),
                ('place3_start_year', models.PositiveIntegerField(blank=True)),
                ('place3_end_year', models.PositiveIntegerField(blank=True)),
            ],
        ),
    ]
