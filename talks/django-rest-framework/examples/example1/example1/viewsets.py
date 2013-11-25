from rest_framework import viewsets

from example1 import models

class MyModelViewSet(viewsets.ModelViewSet):
    model = models.MyModel
