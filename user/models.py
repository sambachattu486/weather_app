from django.db import models

# Create your models here.

class people(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    pin = models.IntegerField()