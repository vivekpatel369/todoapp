from django.db import models
from django.contrib.auth.models import User

class TodoList(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    user = models.ForeignKey(User, unique=False)


class Todos(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    desc = models.CharField(max_length=1000, blank=True, default='')
    status = models.BooleanField(default=False)
    list = models.ForeignKey(TodoList, related_name='todolist')

    def __str__(self):
        return "Title : {0}".format(self.title)