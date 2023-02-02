
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Theme, Post, Comment
from .serializers import ThemeSerializer, PostSerializers, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .service import PostFilter, CommentFilter
from .permissions import IsOwnerOrReadOnly


class ThemeAPIView(generics.ListAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class PostPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    filter_backends = (DjangoFilterBackend, )
    filterset_class = PostFilter
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, ]
    pagination_class = PostPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CommentFilter
    pagination_class = CommentPagination

    def perform_create(self, serializer):
        level = 0
        parent = serializer.validated_data.get('parent_id')
        if parent:
            level = Comment.objects.get(pk=parent.pk).level+1
        serializer.save(author=self.request.user, level=level)

