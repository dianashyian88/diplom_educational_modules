from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import User


class UserTestCase(APITestCase):
    """Авто-тесты для view и serializer User"""

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(username='Тестов Тест Тестович',
                                             email='test1@mail.ru',
                                             password='123456qwerty',
                                             is_staff=True)
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """Тестирование регистрации пользователя"""
        data = {
            "username": "user1",
            "email": "user1@gmail.com",
            "password": "qweasdzxc"
        }

        response = self.client.post(
            '/users/registration/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "email": "user1@gmail.com",
                "username": "user1",
                "phone": None,
                "city": None,
                "telegram_id": None,
                "password": "qweasdzxc",
                "avatar": None
            }
        )

    def test_user_delete(self):
        """Тестирование удаления пользователя"""
        response = self.client.delete(
            '/users/delete/16/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_user_delete_stop(self):
        """Тестирование запрета удаления пользователя"""

        User.objects.create(
            id=2,
            email="user1@user.user",
            password="qweasdzxc"
        )

        response = self.client.delete(
            '/users/delete/2/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_user_detail(self):
        """Тестирование выведения информации о пользователе"""
        response = self.client.get(
            '/users/detail/18/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_list(self):
        """Тестирование выведения списка пользователей"""
        User.objects.create(
            id=20,
            email="user1@user.user",
            password="qweasdzxc"
        )

        response = self.client.get(
            '/users/list/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_update(self):
        """Тестирование обновления информации о пользователе"""
        data = {
            "username": "Тестов Тест",
            "email": "test1@mail.ru",
            "password": "qwerty123456789"
        }

        response = self.client.put(
            '/users/update/20/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class UserModelTestCase(APITestCase):
    """Авто-тесты для модели User"""

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(username='Тестов Тест Тестович',
                                             email='test1@mail.ru',
                                             password='123456qwerty',
                                             is_staff=True)
        self.client.force_authenticate(user=self.user)

    def test_user_view(self):
        """Тестирование строкового представления пользователя"""
        expected_object_name = self.user.email
        self.assertEquals(expected_object_name, str(self.user))
