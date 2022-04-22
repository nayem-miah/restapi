
from rest_framework import serializers
from . models import Tast

class TastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tast
        fields = '__all__'