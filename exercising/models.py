import datetime

from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# class User(models.Model):
#     firstName = models.CharField(max_length = 200)
#     lastName = models.CharField(max_length = 200)
#     identification = models.CharField(max_length = 200)
#     score = models.CharField(max_length = 200)

#     def __str__(self):
#         return self.text

class Exercise_Log(models.Model):
    exercise_type = models.CharField(max_length = 50, default = "")
    duration = models.DecimalField(max_digits = 4, decimal_places = 2, default=0.0)
    date = models.DateField(default=datetime.date.today)
    def __str__(self):
        return str(self.date)

class Profile(models.Model):
    profile = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    logs = models.ManyToManyField(Exercise_Log, blank=True)

    def __str__(self):
        return self.profile.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    for user in User.objects.all():
        Profile.objects.get_or_create(profile=user)