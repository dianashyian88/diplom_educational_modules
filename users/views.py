from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.serializers import UserSerializer
from users.models import User
from users.permissions import IsCurrentUser, IsStaff
from users.services import create_user
from rest_framework.response import Response


class UserCreateAPIView(generics.CreateAPIView):
    """Эндпойнт регистрации пользователя"""
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.data
        password = user['password']
        email = user['email']
        username = user['username']
        phone = user['phone']
        city = user['city']
        telegram_id = user['telegram_id']
        create_user(password, email, username, phone, city, telegram_id)
        return Response(serializer.data)


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпойнт выведения информации о пользователе"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsCurrentUser]
