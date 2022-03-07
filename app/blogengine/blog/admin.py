from django.contrib import admin

from .models import Tag
from .models import Post

admin.site.register(Tag)
admin.site.register(Post)