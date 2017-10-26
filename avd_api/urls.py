from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.authtoken import views
from todoapp.api import TodosListItem, TodosList

urlpatterns = [
    # Examples:
    # url(r'^$', 'avd_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth_api/', include('auth_api.urls')),
    url(r'^todos/$', TodosListItem.as_view()),
    url(r'^todos/(?P<id>[0-9]+)/$', TodosListItem.as_view()),
    url(r'^todoslist/$', TodosList.as_view()),
    url(r'^todoslist/(?P<id>[0-9]+)/$', TodosList.as_view()),
]
