from django.contrib.auth import authenticate, login, logout
from rest_framework import status, views
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from .serializers import TodosSerializer
from .models import Todos


class TodosList(APIView):
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

    def delete(self, request,*args, **kwargs):
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
