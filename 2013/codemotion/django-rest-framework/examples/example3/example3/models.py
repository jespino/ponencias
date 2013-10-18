from django.db import models
from django.contrib.auth.models import User

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    thing = models.IntegerField()
    internal_thing = models.FloatField(null=True, blank=True)
    owner = models.ForeignKey(User)
