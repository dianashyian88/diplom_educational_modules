from rest_framework import serializers
from education.models import Course, Lesson
from education.validators import DescriptionValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [DescriptionValidator(field='description'),
                      DescriptionValidator(field='link_to_video')]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set',
                               many=True,
                               read_only=True)
    subscription_status = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.pk).count()

    class Meta:
        model = Course
        fields = '__all__'
        validators = [DescriptionValidator(field='description')]
