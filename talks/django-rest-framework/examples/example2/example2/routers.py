from rest_framework import routers

from example2 import viewsets

router = routers.DefaultRouter()
router.register('my-model', viewsets.MyModelViewSet)
router.register('no-model', viewsets.NoModelViewSet, 'no-model')
