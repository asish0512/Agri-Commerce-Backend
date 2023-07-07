from rest_framework import serializers

from loads.models import Load

class LoadSerializer(serializers.ModelSerializer):
   class Meta:
       model = Load
       fields = ('goat_count', 'num_male', 'num_female')