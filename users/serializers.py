from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from users.models import User, UserGroup

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'created_at', 'updated_at']
        fields_read_only = ['id', 'created_at', 'updated_at']

class UserSerializer(BaseSerializer):
    '''
    Serializer for User model
    '''
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password', None)
        if password is not None:
            attrs['password'] = make_password(password)
        return super().validate(attrs)
    
class UserGroupSerializer(BaseSerializer):
    '''
    Serializer for User group model
    '''
    class Meta:
        model = UserGroup
        fields = BaseSerializer.Meta.fields + ['name']