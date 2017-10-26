from rest_framework import serializers
# Create your tests here.
from .models import Todos

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos