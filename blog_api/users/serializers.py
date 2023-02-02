
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import User, Profile, Country, Rang
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'nickname', 'password',)

    def validate_password(self, value):
        return make_password(value)


class ProfileSerializer(serializers.ModelSerializer):
    nickname = serializers.StringRelatedField(source='user')
    origin_country_name = serializers.StringRelatedField(source='origin_country')
    rang_name = serializers.StringRelatedField(source='rang')

    class Meta:
        model = Profile

        fields = ('join_date', 'nickname', 'self_information', 'origin_country', 'origin_country_name',
                  'rang', 'rang_name', 'profile_image')
        lookup_field = 'nickname'
        extra_kwargs = {
            'origin_country': {'write_only': True},
            'rang': {'write_only': True},
        }
        read_only_fields = ('nickname', 'origin_country_name', 'rang_name',)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'title', )


class RangSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rang
        fields = ('title',)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['nickname'] = user.nickname

        return token
