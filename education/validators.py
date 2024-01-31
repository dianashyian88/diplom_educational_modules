from rest_framework.serializers import ValidationError
from re import findall


class DescriptionValidator:
    """Валидатор для проверки материалов на наличие недопустимых ссылок"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        urls = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        result = [url for url in findall(urls, tmp_val)]
        if len(result) != 0:
            for item in result:
                if 'youtube.com' not in item:
                    raise ValidationError('Материалы содержат '
                                          'недопустимые ссылки')


class NumberValidator:
    """Валидатор для проверки номера на 0"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val == 0:
            raise ValidationError('Номер не может быть равен 0')
