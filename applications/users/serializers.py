from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation 

from rest_framework import exceptions
from rest_framework.serializers import ModelSerializer, CharField, EmailField
from rest_framework.validators import UniqueValidator

UserModel = get_user_model()

class UserSerializer(ModelSerializer):
    username = CharField(validators=[UniqueValidator(queryset=UserModel.objects.all(), message='A user with that username already exists')])

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'password')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': { 'write_only': True },
        }

    def validate_password(self, value):
        errors = None
        try:
            password_validation.validate_password(password=value)
        except exceptions.ValidationError as error:
            errors = list(error.messages)
        if errors:
            raise serializers.ValidationError(errors[0])
        return value

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class SimpleUserSerializer(ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('id', 'username')
