# Generated by Django 2.2 on 2020-09-25 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationfinder', '0004_auto_20200925_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='birth_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='death_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='fathername',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place1_end_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place1_heigth',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place1_start_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place1_width',
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
            name='place2_end_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place2_heigth',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place2_start_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place2_width',
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
            name='place3_end_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place3_heigth',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place3_start_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formdata',
            name='place3_width',
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
        migrations.AlterField(
            model_name='formdata',
            name='surname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]