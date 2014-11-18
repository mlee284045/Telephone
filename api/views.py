from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.permissions import IsAuthenticatedOrCreate, IsOwnerOrReadOnly
from api.serializers import ProfileSerializer, UserSerializer, TelephoneSerializer
from mobile.models import Profile, Telephone


class UserRegister(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrCreate,)
    
    def post_save(self, obj, created=False):
        """Hashes the password given and saves the updated user"""
        if created:
            obj.set_password(obj.password)
            obj.save()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrCreate,)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (TokenAuthentication,)


class TelephoneViewSet(viewsets.ModelViewSet):
    queryset = Telephone.objects.all()
    serializer_class = TelephoneSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)