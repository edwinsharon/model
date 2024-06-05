from rest_framework import serializers
from .models import person

class Personserializer(serializers.ModelSerializer):
    class meta:
        model = person
        fields='__all__'
        