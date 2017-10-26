from django.contrib.auth import authenticate, login, logout
from rest_framework import status, views
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers

from .serializers import UserSerializer

from django.http import HttpResponse


class LoginDemo(APIView):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password'),
        )
        # token = Token.objects.create(user=user)

        content = {
            'user': user,  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }

        if user is None or not user.is_active:
            return Response({
                'status': 'Unauthorized',
                "message": 'Username or password incorrect'
            }, status=status.HTTP_401_UNAUTHORIZED)
        return Response(UserSerializer(user).data)


class Demo(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response("DEmo")


class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)

# from .serializers import UserSerializer
#
#
# class LoginView(views.APIView):
#     def post(self, request):
#         user = authenticate(
#             username=request.data.get('username'),
#             password=request.data.get('password'),
#         )
#
#         if user is None or not user.is_active:
#             return Response({
#                 'status': 'Unauthorized',
#                 "message": 'Username or password incorrect'
#             }, status=status.HTTP_401_UNAUTHORIZED)
#
#         login(request, user)
#         return Response(UserSerializer(user).data)
#
#
# class LogoutView(views.APIView):
#     def get(self, request):
#         logout(request)
#         return Response({}, status=status.HTTP_204_NO_CONTENT)
