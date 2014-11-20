from django.contrib.auth.models import User
from rest_framework import serializers
from mobile.models import Profile, Telephone


class UserSerializer(serializers.ModelSerializer):
    telephones = serializers.RelatedField(many=True)
    profile = serializers.RelatedField(many=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'telephones', 'profile',)

    def validate_password(self, attrs, source):
        """
        Check that the password created is longer than 4 characters
        """
        password = attrs[source]
        if len(password)<4:
            raise serializers.ValidationError("SHORT!")
        return attrs

    def validate_username(self, attrs, source):
        user = attrs[source]
        password = attrs['password']
        if user == password:
            raise serializers.ValidationError("Your username and password are the same. Change them")
        return attrs


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'picture', 'description',)


class TelephoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Telephone
