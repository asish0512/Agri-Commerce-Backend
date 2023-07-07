from django.db import models

# Create your models here.
class Logistics(models.Model):
    load_id = models.IntegerField(blank=False)
    agent_id = models.IntegerField(blank=False)
    source = models.CharField(blank=False, max_length=20)
    destination = models.CharField(blank=False, max_length=20)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)