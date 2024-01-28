from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserRetrieveAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
    path('registration/', UserCreateAPIView.as_view(),
         name='user-registration'),
    path('detail/<int:pk>/', UserRetrieveAPIView.as_view(),
         name='user-detail'),
]
