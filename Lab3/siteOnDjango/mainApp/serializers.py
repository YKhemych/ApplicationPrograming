from rest_framework import serializers
from mainApp.models import Events

class mainAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'title', 'description', 'date')
