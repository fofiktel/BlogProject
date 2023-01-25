from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import MyTokenObtainPairView, ProfileViewSet, UserViewSet, CountryApiView, RangApiView

urlpatterns = [

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserViewSet.as_view({'post': 'create'}), name='register'),
    path('users/<str:nickname>/', UserViewSet.as_view({'delete': 'destroy', 'patch': 'partial_update'}), name='user_update'),
    path('profile/<str:user__nickname>/',
         ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'}), name='profile'),
    path('countries/', CountryApiView.as_view(), name='countries'),
    path('rangs/', RangApiView.as_view(), name='rang')

]