from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from rest_framework import status, views
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from .serializers import TodosSerializer, TodosListSerializer, TodoDetail
from .models import Todos, TodoList


class TodosListItem(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = TodosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        todos = Todos.objects.all()
        serializer = TodosSerializer(todos, many=True)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        print "ARGS ", args, kwargs
        # print "VIVEK DEMO", request.data
        todos = Todos.objects.get(pk=kwargs.get('id'))
        todos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        todos = Todos.objects.get(pk=kwargs.get('id'))
        serializer = TodosSerializer(todos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodosList(APIView):
    # permission_classes = (IsAuthenticated,)
    def post(self, request):
        serializer = TodosListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        todolist = TodoList.objects.filter(user=request.user)
        serializer = TodoDetail(todolist, many=True)
        return Response(serializer.data)
        # return HttpResponse(Token.objects.get(key='31a0cd7de267a41fd0c3a2db60e8e1a86c97d6c4').user)
