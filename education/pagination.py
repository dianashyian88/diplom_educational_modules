from rest_framework.pagination import PageNumberPagination


class EducationPaginator(PageNumberPagination):
    """Пагинатор для приложения Образовательные модули"""

    page_size = 3
