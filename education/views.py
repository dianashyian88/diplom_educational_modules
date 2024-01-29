from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from education.models import Course, Lesson
from education.serializers import CourseSerializer, LessonSerializer
from education.permissions import IsOwner, IsStaff
from education.pagination import EducationPaginator
from education.tasks import send_mail_create_course


class CourseCreateAPIView(generics.CreateAPIView):
    """Эндпойнт создания курса"""
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Функция сохраняет id пользователя,
        который создает курс, в поле owner"""
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()
        send_mail_create_course.delay(new_course.name)


class CourseListAPIView(generics.ListAPIView):
    """Эндпойнт выведения списка курсов"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [AllowAny]
    pagination_class = EducationPaginator

    def list(self, request, *args, **kwargs):
        """Функция позволяет выводить данные постранично"""
        queryset = Course.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = CourseSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпойнт выведения информации об одном курсе"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]


class CourseUpdateAPIView(generics.UpdateAPIView):
    """Эндпойнт обновления курса"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsStaff | IsOwner]


class CourseDestroyAPIView(generics.DestroyAPIView):
    """Эндпойнт удаления курса"""
    queryset = Course.objects.all()
    permission_classes = [IsOwner]


class LessonCreateAPIView(generics.CreateAPIView):
    """Эндпойнт создания урока"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Функция сохраняет id пользователя,
        который создает урок, в поле owner"""
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """Эндпойнт выведения списка уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = EducationPaginator

    def list(self, request, *args, **kwargs):
        """Функция позволяет выводить данные постранично"""
        queryset = Lesson.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = LessonSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпойнт выведения информации об одном уроке"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Эндпойнт обновления урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsStaff | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Эндпойнт удаления урока"""
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]
