# Generated by Django 2.2 on 2020-10-20 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationfinder', '0008_auto_20201019_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='information',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='relation',
            name='found_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fbRelations_set', to='relationfinder.FormData'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='reference_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rtRelations_set', to='relationfinder.FormData'),
        ),
    ]
