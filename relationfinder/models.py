from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class FormData(models.Model):
    class Meta:
        verbose_name_plural = "Dataforms"
        verbose_name = "Dataform"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="formdata_set", blank=True, null=True)

    first_name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=30, blank=True, null=True)
    fathername = models.CharField(max_length=30, blank=True, null=True) 

    birth_year = models.PositiveIntegerField(blank=True, null=True)
    death_year = models.PositiveIntegerField(blank=True, null=True)

    place1_x = models.FloatField(blank=True, null=False, default=10000.0)
    place1_y = models.FloatField(blank=True, null=False, default=10000.0)
    place1_radius = models.FloatField(blank=True, null=False, default=-1.0)
    place1_start_year = models.PositiveIntegerField(blank=True, null=True)
    place1_end_year = models.PositiveIntegerField(blank=True, null=True)

    place2_x = models.FloatField(blank=True, null=False, default=10000.0)
    place2_y = models.FloatField(blank=True, null=False, default=10000.0)
    place2_radius = models.FloatField(blank=True, null=False, default=-1.0)
    place2_start_year = models.PositiveIntegerField(blank=True, null=True)
    place2_end_year = models.PositiveIntegerField(blank=True, null=True)
    
    place3_x = models.FloatField(blank=True, null=False, default=10000.0)
    place3_y = models.FloatField(blank=True, null=False, default=10000.0)
    place3_radius = models.FloatField(blank=True, null=False, default=-1.0)
    place3_start_year = models.PositiveIntegerField(blank=True, null=True)
    place3_end_year = models.PositiveIntegerField(blank=True, null=True)

    information = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{} {} {} ({})'.format(self.surname, self.first_name, self.fathername, str(self.user))



class UserExtension(models.Model):
    user = models.OneToOneField(User,null=True, blank=True, on_delete=models.CASCADE, related_name='userExtension')
    first_name = models.CharField(max_length=30,blank=True,null=True)
    surname = models.CharField(max_length=30,blank=True,null=True)
    fathername = models.CharField(max_length=30,blank=True,null=True)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    information = models.TextField(blank=True,null=True)
    photo = models.ImageField(blank=True, null=True, default="def_profile_photo.png")

class Message(models.Model):
    written_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="wtMessages_set")
    written_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="wbMessages_set")
    text = models.TextField(blank=True, null=True)


class Relation(models.Model):
    found_by = models.ForeignKey(FormData, on_delete=models.CASCADE, blank=True, null=True, related_name="fbRelations_set") 
    reference_to = models.ForeignKey(FormData, on_delete=models.CASCADE, blank=True, null=True, related_name="rtRelations_set")
    similarity = models.FloatField(null=True, blank=True)