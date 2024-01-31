from rest_framework import serializers
from education.models import Course, Lesson
from education.validators import DescriptionValidator, \
    NumberValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [DescriptionValidator(field='description'),
                      DescriptionValidator(field='link_to_video')]


class CourseSerializer(serializers.ModelSerializer):
    course_number = serializers.SerializerMethodField()
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set',
                               many=True,
                               read_only=True)

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.pk).count()

    def get_course_number(self, obj):
        course_list = Course.objects.all()
        number = 0
        dict_number = {}
        for course in course_list:
            number += 1
            pk = str(course.pk)
            dict_number[pk] = number
        course_number = dict_number[str(obj.pk)]
        return course_number

    class Meta:
        model = Course
        fields = '__all__'
        validators = [DescriptionValidator(field='description'),
                      NumberValidator(field='number')]
