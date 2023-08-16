import os 
from rest_framework.pagination import PageNumberPagination
from dotenv import load_dotenv

load_dotenv()


class CommentsPagination(PageNumberPagination):
    """Паджинатор для моделей News."""
    comments_size = os.getenv('SIZE_COMMENTS_PAGINATION', default=10)
