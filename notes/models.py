from django.conf import settings
from django.db import models
from django.utils import timezone


class Note(models.Model):
    author = models.TextField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isPin = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title