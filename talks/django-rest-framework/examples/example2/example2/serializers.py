from rest_framework import serializers
from example2.models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ('id', 'name', 'thing', 'owner')
