from education.apps import EducationConfig
from education.views import LessonCreateAPIView, LessonListAPIView, \
    LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView, \
    CourseCreateAPIView, CourseListAPIView, CourseRetrieveAPIView, \
    CourseUpdateAPIView, CourseDestroyAPIView
from django.urls import path

app_name = EducationConfig.name

urlpatterns = [
    path('', CourseListAPIView.as_view(),
         name='home'),
    path('course/create/', CourseCreateAPIView.as_view(),
         name='course-create'),
    path('course/<int:pk>/', CourseRetrieveAPIView.as_view(),
         name='course-detail'),
    path('course/update/<int:pk>/', CourseUpdateAPIView.as_view(),
         name='course-update'),
    path('course/delete/<int:pk>/', CourseDestroyAPIView.as_view(),
         name='course-delete'),
    path('lesson/create/', LessonCreateAPIView.as_view(),
         name='lesson-create'),
    path('lesson/list/', LessonListAPIView.as_view(),
         name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(),
         name='lesson-detail'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(),
         name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(),
         name='lesson-delete'),

]
