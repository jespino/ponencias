from rest_framework import serializers
from example3.models import MyModel

class MyModelSerializer(serializers.ModelSerializer):
    method_field = serializers.SerializerMethodField('get_method_field_data')
    private_data = serializers.Field(source='internal_thing')

    def get_method_field_data(self, obj):
        return "This is a method generated data!"

    class Meta:
        model = MyModel
        fields = ('id', 'name', 'thing', 'owner', 'private_data', 'method_field')
