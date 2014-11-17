from django.contrib.auth.models import User
from rest_framework import serializers
from mobile.models import Profile, Telephone


class UserSerializer(serializers.ModelSerializer):
    telephones

    class Meta:
        model = User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile


class TelephoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telephone