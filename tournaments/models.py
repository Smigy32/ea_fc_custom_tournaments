from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=200)
    flag = models.ImageField()
    
class Club(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)