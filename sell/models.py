from django.db import models

# Create your models here.

class Selltran(models.Model):
    load_id = models.IntegerField(blank=False)
    agent_id = models.IntegerField(blank=False)
    seller_id = models.IntegerField(blank=False)
    source = models.CharField(blank=False, max_length=20)
    amount_due = models.FloatField(blank=False)
    due_time = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)