from rest_framework import routers

from example1 import viewsets

router = routers.DefaultRouter()
router.register('my-model', viewsets.MyModelViewSet)
