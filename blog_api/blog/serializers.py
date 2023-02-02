
from rest_framework import serializers
from .models import Theme, Post, Comment
from users.models import Profile, User
from users.serializers import ProfileSerializer
from blog_api.settings import BASE_DIR

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('id', 'title', )


class PostSerializers(serializers.ModelSerializer):
    theme_name = serializers.StringRelatedField(source='theme', many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'content', 'theme_name', 'theme')
        extra_kwargs = {
            'theme': {'write_only': True},
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author_profile'] = {
            'nickname': instance.author.nickname,
            'image': ProfileSerializer(Profile.objects.get(user=instance.author)).data['profile_image'],
        }
        return data


class CommentSerializer(serializers.ModelSerializer):
    children = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ('id','author','post','parent_id','level', 'text', 'children', )
        extra_kwargs = {
            'level': {'read_only': True},
            'author': {'write_only': True}
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author_profile'] = {'nickname': instance.author.nickname,
                                   'image': ProfileSerializer(Profile.objects.get(user=instance.author)).data['profile_image']}
        return data