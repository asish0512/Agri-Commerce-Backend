from django.db import models

# Create your models here.
class Load(models.Model):
    goat_count = models.IntegerField(default=0)
    num_male = models.IntegerField(default=0)
    num_female  = models.IntegerField(default=0)
    value_load = models.FloatField(default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)