from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализация пользователя"""

    class Meta:
        model = User
        fields = ['email',
                  'username',
                  'phone',
                  'city',
                  'telegram_id',
                  'password',
                  'avatar'
                  ]
