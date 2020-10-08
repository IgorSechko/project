# Generated by Django 2.2 on 2020-10-08 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('relationfinder', '0006_auto_20200928_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdata',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='formdata', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True)),
                ('surname', models.CharField(blank=True, max_length=30, null=True)),
                ('fathername', models.CharField(blank=True, max_length=30, null=True)),
                ('birth_date', models.DateTimeField(blank=True, null=True)),
                ('information', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userdetails', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
