from rest_framework import serializers

from goats.models import Goat, GoatsInLoad

class GoatSerializer(serializers.ModelSerializer):
   class Meta:
       model = Goat
       fields = ('sex', 'breed', 'weight','price', 'photo_url')
       
class GoatsInLoadSerializer(serializers.ModelSerializer):
   class Meta:
       model = GoatsInLoad
       fields = ('load_id','goat_id','status')