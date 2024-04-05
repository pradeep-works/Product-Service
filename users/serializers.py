from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from users.models import User

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'created_at', 'updated_at']
        fields_read_only = ['id', 'created_at', 'updated_at']

class UserSerializer(BaseSerializer):
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