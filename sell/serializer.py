from rest_framework import serializers

from sell.models import Selltran

class SellSerializer(serializers.ModelSerializer):
   class Meta:
       model = Selltran
       fields = ('load_id', 'agent_id', 'seller_id', 'source', 'amount_due', 'due_time')
       