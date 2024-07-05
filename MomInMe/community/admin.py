from django.contrib import admin
from .models import Post,Like

#주석추가
admin.site.register(Post)
admin.site.register(Like)