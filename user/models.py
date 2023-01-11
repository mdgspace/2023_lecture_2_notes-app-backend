from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    username = models.TextField(primary_key = True)
    password = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.username