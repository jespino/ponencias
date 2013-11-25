from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from example2 import models
from example2.filters import IsOwnerFilterBackend
from example2.serializers import MyModelSerializer

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = models.MyModel.objects.all()
    serializer_class = MyModelSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    filter_backends = (IsOwnerFilterBackend, filters.OrderingFilter,)
    paginate_by = 10
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class NoModelViewSet(viewsets.ViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        return Response([{'hello': 'list'}])

    def retrieve(self, request, pk=None):
        return Response({'hello': pk})

    def create(self, request):
        return Response({'hello': 'create', 'data': request.DATA})

    def update(self, request, pk=None):
        return Response({'hello': pk, 'data': request.DATA})

    def partial_update(self, request, pk=None):
        return Response({'hello': pk, 'data': request.DATA})

    def destroy(self, request, pk=None):
        return Response({'hello': pk})
