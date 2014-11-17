from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import ProfileSerializer, UserSerializer, TelephoneSerializer
from mobile.models import Profile, Telephone


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class TelephoneViewSet(viewsets.ModelViewSet):
    queryset = Telephone.objects.all()
    serializer_class = TelephoneSerializer