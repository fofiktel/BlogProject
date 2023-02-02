from django_filters import rest_framework as filters
from .models import Post, Comment


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PostFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='author__nickname')
    theme = CharFilterInFilter(field_name='theme__title')

    class Meta:
        model = Post
        fields = ('author', 'theme')


class CommentFilter(filters.FilterSet):
    author = filters.CharFilter(field_name='author__nickname')
    post = filters.NumberFilter(field_name='post__pk')

    class Meta:
        model = Comment
        fields = ('author', 'post')

