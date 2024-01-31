from django.db import models
from config.settings import AUTH_USER_MODEL
from users.models import NULLABLE


class Course(models.Model):
    """Модель образовательных модулей (курсов)"""
    name = models.CharField(max_length=50,
                            verbose_name='наименование')
    image = models.ImageField(upload_to='course/',
                              verbose_name='изображение',
                              **NULLABLE)
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              verbose_name='пользователь',
                              **NULLABLE)
    update_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name='дата обновления курса',
        **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('id',)


class Lesson(models.Model):
    """Модель уроков в рамках каждого модуля (курса)"""
    name = models.CharField(max_length=100,
                            verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    link_to_video = models.URLField(
        max_length=200,
        verbose_name='ссылка на видео',
        **NULLABLE)
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               verbose_name='курс',
                               **NULLABLE)
    owner = models.ForeignKey(AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              verbose_name='пользователь',
                              **NULLABLE)
    update_date = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name='дата обновления',
        **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('id',)
