
from rest_framework import generics, viewsets
from .models import Theme, Post
from .serializers import ThemeSerializer, PostSerializers


class ThemeAPIView(generics.ListAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
# Create your views here.
