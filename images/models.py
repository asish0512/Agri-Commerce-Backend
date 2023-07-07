from django.db import models

# Create your models here.
class Image(models.Model):
    goat_id = models.IntegerField(blank=False)
    image = models.TextField(blank=False)