from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Place (models.Model):
    title = models.CharField(max_length=200)
    description_short  = models.TextField(max_length=300)
    description_long = models.TextField()
    lng = models.FloatField( blank=True, null=True)
    lat = models.FloatField( blank=True, null=True)

    def __str__(self):
        return self.title