from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterAPIView
from django.urls import path

urlpatterns = [
   
    path('register/author/',RegisterAPIView.as_view(), name = 'register-author'),
    path('register/customer/',RegisterAPIView.as_view(), name = 'register-visitor' ),
    path('login/author/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/customer/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
]