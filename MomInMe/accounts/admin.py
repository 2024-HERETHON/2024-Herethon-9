# admin.py

from django.contrib import admin
from .models import UserProfile,MeKeyword,BabyKeyword

admin.site.register(UserProfile)
admin.site.register(MeKeyword)
admin.site.register(BabyKeyword)
