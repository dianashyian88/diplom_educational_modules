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
        """Функция получает данные от пользователя при регистрации,
        передает их в функцию создания пользователя и сохраняет пользователя"""
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
    permission_classes = [IsCurrentUser | IsStaff]


class UserListAPIView(generics.ListAPIView):
    """Эндпойнт выведения списка пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsStaff]


class UserUpdateAPIView(generics.UpdateAPIView):
    """Эндпойнт обновления информации о пользователе"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsCurrentUser | IsStaff]


class UserDestroyAPIView(generics.DestroyAPIView):
    """Эндпойнт удаления пользователя"""
    queryset = User.objects.all()
    permission_classes = [IsCurrentUser]
