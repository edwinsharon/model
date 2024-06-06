from rest_framework import serializers
from .models import person

class Peopleserializer(serializers.ModelSerializer):
    class meta:
        model = person
        fields='__all__'
        