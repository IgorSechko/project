from django.db import models
from django.conf import settings
import random

User = settings.AUTH_USER_MODEL

# Create your models here.


class Tweet(models.Model):
    # id = models.AutoField(primary_key = True)
    # a user can have many tweets, a tweet has only one user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # cascade: owner deleted - all the tweets also deleted
    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-id']

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 51)
        }
