import datetime

from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.urls import reverse


class Exercise_Log(models.Model):
    exercise_type = models.CharField(max_length = 50, default = "")
    duration = models.DecimalField(max_digits = 4, decimal_places = 2, default=0.0)
    date = models.DateField(default=datetime.date.today)
    def __str__(self):
        return str(self.date)

class Goal_Log(models.Model):
    exercise_type = models.CharField(max_length = 50, default = "")
    duration = models.DecimalField(max_digits = 4, decimal_places = 2, default=0.0)
    def __str__(self):
        return str(self.exercise_type)

class Group(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField()
    members = models.ManyToManyField(User, related_name="members")
    owner = models.ForeignKey(User, related_name="owner", on_delete = models.CASCADE)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('group_detail', args=[str(self.id)])
    
class Message(models.Model):
    post = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, null=False, default="no author")

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.description, self.author)




class Profile(models.Model):
    profile = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    logs = models.ManyToManyField(Exercise_Log, blank=True)
    goals = models.ManyToManyField(Goal_Log, blank=True)

    def __str__(self):
        return self.profile.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    for user in User.objects.all():
        Profile.objects.get_or_create(profile=user)
