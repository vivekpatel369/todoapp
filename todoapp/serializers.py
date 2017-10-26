from rest_framework import serializers
from django.contrib.auth.models import User
# Create your tests here.
from .models import Todos, TodoList

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos

class TodosListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('title',)

class TodoDetail(serializers.ModelSerializer):
    todolist = TodosSerializer(many=True)
    class Meta:
        model= TodoList
        fields = ('id','title' ,'todolist')