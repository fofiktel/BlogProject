from django.urls import path
from .views import ThemeAPIView, PostViewSet, CommentViewSet

urlpatterns = [
    path('themes/', ThemeAPIView.as_view(), name='themes'),
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('posts/<int:pk>',PostViewSet.as_view({'get': 'retrieve','put': 'update', 'patch': 'partial_update'})),
    path('comments/',CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('comments/<int:pk>', CommentViewSet.as_view({'delete': 'destroy', 'patch': 'partial_update'}))
]