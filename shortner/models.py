from django.db import models


# Create your models here.
class Link(models.Model):
    prefix = models.CharField(max_length=6)
    link = models.CharField(max_length=100)