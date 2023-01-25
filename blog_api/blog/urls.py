from django.urls import path
from .views import ThemeAPIView, PostViewSet

urlpatterns = [
    path('themes/', ThemeAPIView.as_view(), name='themes'),
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create'}))
]