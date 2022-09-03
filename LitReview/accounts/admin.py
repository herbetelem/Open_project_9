from django.contrib import admin
from .models import UserTheme, UserFollows

# Register your models here.
admin.site.register(UserTheme)
admin.site.register(UserFollows)