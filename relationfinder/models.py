from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.


def override_username(self):
    name = '{} {} {}'.format(self.userExtension.surname,
                             self.userExtension.first_name, self.userExtension.fathername)
    return name


User.add_to_class("__str__", override_username)


class Card(models.Model):
    class Meta:
        verbose_name_plural = "Cards"
        verbose_name = "Card"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="card_set", blank=True, null=True)
    card_name = models.CharField(
        max_length=30, blank=False, null=False, default="default name")

    sex = models.CharField(max_length=30, blank=False,
                           null=False, default="default")
    relation_level = models.CharField(
        max_length=30, blank=False, null=False, default="default")

    first_name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=30, blank=True, null=True)
    fathername = models.CharField(max_length=30, blank=True, null=True)

    birth_year = models.PositiveIntegerField(blank=True, null=True)
    death_year = models.PositiveIntegerField(blank=True, null=True)

    place1_x = models.FloatField(blank=True, null=True)
    place1_y = models.FloatField(blank=True, null=True)
    place1_radius = models.FloatField(blank=True, null=True)
    place1_start_year = models.PositiveIntegerField(blank=True, null=True)
    place1_end_year = models.PositiveIntegerField(blank=True, null=True)

    place2_x = models.FloatField(blank=True, null=True)
    place2_y = models.FloatField(blank=True, null=True)
    place2_radius = models.FloatField(blank=True, null=True)
    place2_start_year = models.PositiveIntegerField(blank=True, null=True)
    place2_end_year = models.PositiveIntegerField(blank=True, null=True)

    place3_x = models.FloatField(blank=True, null=True)
    place3_y = models.FloatField(blank=True, null=True)
    place3_radius = models.FloatField(blank=True, null=True)
    place3_start_year = models.PositiveIntegerField(blank=True, null=True)
    place3_end_year = models.PositiveIntegerField(blank=True, null=True)

    information = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{} {} {} ({} для {}) '.format(self.surname, self.first_name, self.fathername, self.relation_level, str(self.user))

    def save(self, *args, **kwargs):
        if self.first_name:
            self.first_name = self.first_name.capitalize()
        if self.surname:
            self.surname = self.surname.capitalize()
        if self.fathername:
            self.fathername = self.fathername.capitalize()
        return super(Card, self).save(*args, **kwargs)


class UserExtension(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name='userExtension')
    first_name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=30, blank=True, null=True)
    fathername = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    photo = models.ImageField(blank=True, null=True,
                              default="def_profile_photo.png")

    def __str__(self):
        return '{} {} {}'.format(self.surname, self.first_name, self.fathername)


class Message(models.Model):
    written_to = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="wtMessages_set")
    written_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="wbMessages_set")
    text = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True, blank=True, null=False)


class Relation(models.Model):
    referenced_by = models.ForeignKey(
        Card, on_delete=models.CASCADE, blank=True, null=True, related_name="fbRelations_set")
    referencing = models.ForeignKey(
        Card, on_delete=models.CASCADE, blank=True, null=True, related_name="rtRelations_set")
    connection_type = models.CharField(max_length=30, blank=True, null=True)
    similarity = models.FloatField(null=True, blank=True)
