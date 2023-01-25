
from rest_framework import serializers
from .models import Theme, Post
from users.models import Profile, User
from users.serializers import ProfileSerializer


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'title', )


class PostSerializers(serializers.ModelSerializer):
    theme_name = serializers.StringRelatedField(source='theme', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('content', 'theme_name', 'theme')
        extra_kwargs = {
            'theme': {'write_only': True},
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['profile'] = {'nickname': instance.author.nickname,
                           'image': ProfileSerializer(Profile.objects.get(user=instance.author)).data['profile_image']}
        return data


