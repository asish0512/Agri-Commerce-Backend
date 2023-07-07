from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(blank=False, max_length=25)
    user_type = models.CharField(blank=False, max_length=10)
