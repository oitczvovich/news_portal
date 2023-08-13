from django.contrib import admin

from user.models import User
from news.models import News
from comments.models import Comment


models = [
    User,
    News,
    Comment
]

admin.site.register(models)
