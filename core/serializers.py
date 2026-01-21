from rest_framework import serializers
from .exceptions import CustomValidationError
from .models import User,Car

class SingUpSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

    def create(self, validated_data):
        username=validated_data['username']
        password=validated_data['password']

        user=User(username=username)
        user.set_password(password)

        user.save()
        
        return user
    
    def validate_username(self,username):
        if User.objects.filter(username=username).exists():
            raise CustomValidationError(detail='This username already exists')
        return username

class CarSerializer(serializers.Serializer):
    class Meta:
        model=Car
        fields=['id','brand','year','mileage','engine_power','price','user']