from django.db import models
from django.urls import reverse

NAMES = (
    ('B', 'Brandy'),
    ('G', 'Gin'),
    ('M', 'Mezcal'),
    ('R', 'Rum'),
    ('M', 'Mezcal'),
    ('T', 'Tequila'),
    ('V', 'Vodka')
)

# Create your models here.
class Liquor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=150)
    ABV = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'liquor_id': self.id})
    

class Spirit(models.Model):
    name = models.CharField(
        max_length=1,
        choices=NAMES,
        default=NAMES[0][0]
    )

    liquor = models.ForeignKey(
        Liquor,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.get_name_display()} on {self.date}"
    
    class Meta:
        ordering = []