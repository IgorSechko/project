# Generated by Django 2.2 on 2020-10-19 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('relationfinder', '0007_auto_20201018_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('similarity', models.FloatField(blank=True, null=True)),
                ('found_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fbRelations_set', to=settings.AUTH_USER_MODEL)),
                ('reference_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rtRelations_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
        migrations.AlterField(
            model_name='formdata',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formdata_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Relations',
        ),
    ]
