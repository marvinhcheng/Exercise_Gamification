from django.contrib import admin
from .models import Profile, Exercise_Log, Goal_Log
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Profile)
admin.site.register(Exercise_Log)
admin.site.register(Goal_Log)