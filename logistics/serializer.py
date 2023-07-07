from rest_framework import serializers

from logistics.models import Logistics

class LogisticsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Logistics
       fields = ('load_id', 'agent_id', 'source', 'destination')
       
