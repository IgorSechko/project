# Generated by Django 2.2 on 2020-10-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationfinder', '0010_auto_20201020_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='place1_radius',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place1_x',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place1_y',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place2_radius',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place2_x',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place2_y',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place3_radius',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place3_x',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place3_y',
            field=models.FloatField(blank=True, null=True),
        ),
    ]