from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import User
from education.models import Course, Lesson


class CourseTestCase(APITestCase):
    """Авто-тесты для view Course"""

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(username='Тестов Тест Тестович',
                                             email='test1@mail.ru',
                                             password='123456qwerty')
        self.client.force_authenticate(user=self.user)

    def test_course_create(self):
        """Тестирование создания курса с валидацией
        описания"""
        data = {
                    "name": "Основы ПДД",
                    "description": "Коротко о курсе: https://youtube.com"
        }
        response = self.client.post(
            '/course/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_course_delete(self):
        """Тестирование удаления курса"""
        Course.objects.create(
            id=1,
            name="Основы финансовой грамотности",
            description="Основы финансовой грамотности",
            owner=self.user
        )

        response = self.client.delete(
            '/course/delete/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_course_detail(self):
        """Тестирование выведения информации о курсе"""
        Course.objects.create(
            id=1,
            name="Основы финансовой грамотности",
            description="Основы финансовой грамотности",
            owner=self.user
        )

        response = self.client.get(
            '/course/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_course_list(self):
        """Тестирование выведения списка курсов"""
        Course.objects.create(
            id=1,
            name="Основы финансовой грамотности",
            description="Основы финансовой грамотности",
            owner=self.user
        )

        response = self.client.get(
            ''
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_course_update(self):
        """Тестирование обновления информации о курсе"""
        Course.objects.create(
            id=1,
            name="Основы финансовой грамотности",
            description="Основы финансовой грамотности",
            owner=self.user
        )

        data = {
            "name": "Основы финансовой грамотности",
            "description": "http://youtube.com/check?uri=ert"
        }

        response = self.client.put(
            '/course/update/1/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class LessonTestCase(APITestCase):
    """Авто-тесты для view Lesson"""

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(username='Тестов Тест Тестович',
                                             email='test1@mail.ru',
                                             password='123456qwerty')
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        """Тестирование создания урока с валидацией ссылки и описания"""
        data = {
            "name": "Участники ДД",
            "link_to_video": "http://youtube.com/check?uri=ert",
            "description": "В этом уроке вы узнаете..."
        }
        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_lesson_delete(self):
        """Тестирование удаления урока"""
        Lesson.objects.create(
            id=1,
            name="Урок 13. DRF",
            link_to_video="http://youtube.com/check?uri=",
            description="В этом урок вы изучите DRF",
            owner=self.user
        )

        response = self.client.delete(
            '/lesson/delete/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_lesson_detail(self):
        """Тестирование выведения информации об уроке"""
        Lesson.objects.create(
            id=1,
            name="Урок 13. DRF",
            link_to_video="http://youtube.com/check?uri=",
            description="В этом урок вы изучите DRF",
            owner=self.user
        )

        response = self.client.get(
            '/lesson/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_list(self):
        """Тестирование выведения списка уроков"""
        Lesson.objects.create(
            id=1,
            name="Урок 13. DRF",
            link_to_video="http://youtube.com/check?uri=",
            description="В этом урок вы изучите DRF",
            owner=self.user
        )

        response = self.client.get(
            '/lesson/list/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_lesson_update(self):
        """Тестирование обновления информации об уроке"""
        Lesson.objects.create(
            id=1,
            name="Урок 13. DRF",
            link_to_video="http://youtube.com/check?uri=",
            description="В этом урок вы изучите DRF",
            owner=self.user
        )

        data = {
            "name": "Урок 13. DRF PRO",
            "link_to_video": "http://youtube.com/check?uri=ert",
            "description": "В этом урок вы изучите DRF на..."
        }

        response = self.client.put(
            '/lesson/update/1/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class LessonSerializerTestCase(APITestCase):
    """Авто-тесты для LessonSerializer"""

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(username='Тестов Тест Тестович',
                                             email='test1@mail.ru',
                                             password='123456qwerty')
        self.client.force_authenticate(user=self.user)

    def test_lesson_validate(self):
        """Тестирование валидации урока"""
        data = {
            "name": "Участники ДД",
            "link_to_video": "http://sky.com/check?uri=ert",
            "description": "В этом уроке вы узнаете..."
        }
        response = self.client.post(
            '/lesson/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )


class CourseSerializerTestCase(APITestCase):
    """Авто-тесты для CourseSerializer"""

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create_user(username='Тестов Тест Тестович',
                                             email='test1@mail.ru',
                                             password='123456qwerty')
        self.client.force_authenticate(user=self.user)

    def test_course_validate(self):
        """Тестирование валидации курса"""
        data = {
                    "name": "Основы ПДД",
                    "description": "https://skyeng.com"
        }
        response = self.client.post(
            '/course/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )


class CourseModelTestCase(APITestCase):
    """Авто-тесты для модели Course"""

    def setUp(self) -> None:
        Course.objects.create(
            id=1,
            name="Основы финансовой грамотности",
            description="Основы финансовой грамотности",
        )

    def test_course_view(self):
        """Тестирование строкового представления курса"""
        course = Course.objects.get(id=1)
        expected_object_name = course.name
        self.assertEquals(expected_object_name, str(course))


class LessonModelTestCase(APITestCase):
    """Авто-тесты для модели Lesson"""

    def setUp(self) -> None:
        Lesson.objects.create(
            id=1,
            name="Урок 13. DRF",
            link_to_video="http://youtube.com/check?uri=",
            description="В этом урок вы изучите DRF"
        )

    def test_course_view(self):
        """Тестирование строкового представления урока"""
        lesson = Lesson.objects.get(id=1)
        expected_object_name = lesson.name
        self.assertEquals(expected_object_name, str(lesson))
