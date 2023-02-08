from django.db import models
from django.urls import reverse

# Create your models here.
class Liquor(models.Model):
    name = models.CharField(max_length=50)
    spirit = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    ABV = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'liquor_id': self.id})