from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import detail_route
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
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


class AuthView(APIView):
    authentication_classes = (BasicAuthentication,)

    def post(self, request, *args, **kwargs):
        login(request, request.user)
        return Response(UserSerializer(request.user).data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (BasicAuthentication,)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = (BasicAuthentication,)


class TelephoneViewSet(viewsets.ModelViewSet):
    queryset = Telephone.objects.all()
    serializer_class = TelephoneSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user
        obj.get_sound_url()

    @detail_route(methods=['post'])
    def pass_it_on(self, request, pk):
        changed_text = request.DATA.get('text')
        orig = Telephone.objects.get(pk=pk)
        copy = orig.pass_it_on(changed_text, request.user)
        copy.get_sound_url()
        copy.save()
        print copy.sound_url
        return Response(status=status.HTTP_200_OK)
