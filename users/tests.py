from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class UserTestCase(APITestCase):
    """Авто-тесты для User"""

    def setUp(self) -> None:
        pass

    def test_user_create(self):
        """Тестирование регистрации пользователя"""
        pass

    def test_user_delete(self):
        """Тестирование удаления пользователя"""
        pass

    def test_user_detail(self):
        """Тестирование выведения информации о пользователе"""
        pass

    def test_user_list(self):
        """Тестирование выведения списка пользователей"""
        pass

    def test_user_update(self):
        """Тестирование обновления информации о пользователе"""
        pass
