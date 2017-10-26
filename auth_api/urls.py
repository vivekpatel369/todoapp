from django.conf.urls import url

# from .api import LoginView,LogoutView
from rest_framework.authtoken import views

from .api import LoginDemo, Demo

urlpatterns = [
    url(r'^login/', LoginDemo.as_view()),
    url(r'^demo/', Demo.as_view()),
    url(r'^api-token-auth/', views.obtain_auth_token)
    # url(r'^login/', LoginView.as_view()),
    # url(r'^logout/', LogoutView.as_view()),
]
