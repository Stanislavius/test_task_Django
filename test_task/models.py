from django.db import models
from django.db.models import Model

class Measurement(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField()
    byWho = models.CharField(max_length=100)
