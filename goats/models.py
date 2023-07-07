from django.db import models

# Create your models here.

class Goat(models.Model):
    sex = models.CharField(blank=False, max_length=10)
    breed = models.CharField(blank=False, max_length=20)
    weight = models.FloatField(blank=False)
    price = models.FloatField(blank=False)
    photo_url = models.URLField(blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
class GoatsInLoad(models.Model):
    load_id = models.IntegerField(blank=False)
    goat_id = models.IntegerField(blank=False)
    status = models.BooleanField(blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    
    

