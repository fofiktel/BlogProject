import os

from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from .models import User, Profile, Rang, Country
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, MyTokenObtainPairSerializer, ProfileSerializer, CountrySerializer,\
    RangSerializer
from .permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'nickname'

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     path_to_avatar = Profile.objects.get(user=instance).profile_image.path
    #
    #     if path_to_avatar.find('default_avatar.jpg') == -1:
    #         os.remove(path_to_avatar)
    #     instance.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = 'user__nickname'
   # permission_classes = [IsOwnerOrReadOnly, ]


class CountryApiView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class RangApiView(generics.ListAPIView):
    queryset = Rang.objects.all()
    serializer_class = RangSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
