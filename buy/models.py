from django.db import models

# Create your models here.
class BuyTran(models.Model):
    buyer_id = models.IntegerField(blank=False)
    place = models.CharField(blank=False, max_length=20)
    amount_due = models.FloatField(blank=False)
    due_time = models.IntegerField(blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
class BuyerGoatMap(models.Model):
    buy_id = models.IntegerField(blank=False)
    goat_id = models.IntegerField(blank=False)