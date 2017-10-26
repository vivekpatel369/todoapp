from django.db import models

class Todos(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    desc = models.CharField(max_length=1000, blank=True, default='')
    status = models.BooleanField(default=False)

    def __str__(self):
        return "Title : {0}".format(self.title)