from rest_framework import serializers
from .models import States

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = '__all__'
        # fields = ('id', 'name', 'capital') 