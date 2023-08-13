from rest_framework.pagination import PageNumberPagination


class TitleGenreCategoryPagination(PageNumberPagination):
    """Паджинатор для моделей News."""

    page_size = 5
