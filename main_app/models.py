from django.db import models

# Create your models here.
class Liquor(models.Model):
    name = models.CharField(max_length=50)
    spirit = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    ABV = models.IntegerField()