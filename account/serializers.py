from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from account.models import CustomUser, CustomProfileManager


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['user_name', 'email', 'first_name', 'last_name', 'avatar',
                  'status', 'country', 'city', 'birth']

    def create(self, validated_data):
        obj = super(UserSerializer, self).create(validated_data)
        return obj

    def to_representation(self, instance: CustomUser):
        obj = super(UserSerializer, self).to_representation(instance)
        obj['followers'] = instance.followers.count()
        obj['following'] = instance.following.count()
        return obj


class UserRegisterSerializer(serializers.ModelSerializer):
    login = serializers.CharField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['login', 'email', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            login=validated_data['login'],
            email=validated_data['email'],
            user_name=validated_data['login'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



