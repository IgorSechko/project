from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class FormData(models.Model):
    class Meta:
        verbose_name_plural = "Dataforms"
        verbose_name = "Dataform"

    first_name = models.CharField(max_length=30, blank=True)
    surname = models.CharField(max_length=30, blank=True)
    fathername = models.CharField(max_length=30, blank=True) 

    birth_year = models.PositiveIntegerField(blank=True)
    death_year = models.PositiveIntegerField(blank=True)

    place1_x = models.FloatField(blank=True)
    place1_width = models.FloatField(blank=True)
    place1_y = models.FloatField(blank=True)
    place1_heigth = models.FloatField(blank=True)
    place1_start_year = models.PositiveIntegerField(blank=True)
    place1_end_year = models.PositiveIntegerField(blank=True)

    place2_x = models.FloatField(blank=True)
    place2_width = models.FloatField(blank=True)
    place2_y = models.FloatField(blank=True)
    place2_heigth = models.FloatField(blank=True)
    place2_start_year = models.PositiveIntegerField(blank=True)
    place2_end_year = models.PositiveIntegerField(blank=True)
    
    place3_x = models.FloatField(blank=True)
    place3_width = models.FloatField(blank=True)
    place3_y = models.FloatField(blank=True)
    place3_heigth = models.FloatField(blank=True)
    place3_start_year = models.PositiveIntegerField(blank=True)
    place3_end_year = models.PositiveIntegerField(blank=True)