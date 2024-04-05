from rest_framework import serializers
from retest_app.models import Product

class BaseSerializer(serializers.ModelSerializer):
    '''
    Base serializer for all retest_app serializers
    '''
    class Meta:
        fields = ['id', 'created_at', 'updated_at']
        fields_read_only = ['id', 'created_at', 'updated_at']

class ProductSerializer(BaseSerializer):
    '''
    Serializer method for Product model
    '''
    class Meta:
        model = Product
        fields = BaseSerializer.Meta.fields + ['name', 'price', 'manufacturing_date', 'expiry_date']