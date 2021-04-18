import datetime
from django.db import models
from django.utils import timezone
from django import forms, template
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.urls import reverse

register = template.Library


# excercise_types = (
#     ("CARDIO", "Cardio"),
#     ("WEIGHT_TRAINING", "Weight Training")
#     ("FLEXIBILITY", "Flexibility")
# )

# muscle_regions = (
#     ("ARMS", "Arms"),
#     ("LEGS", "Legs"),
#     ("BACK", "Back"),
#     ("CORE", "Core"),
#     ("CHEST", "Chest"),
# )

exercises = (
    ("CARDIO", "Cardio"),
    ("WEIGHT_TRAINING", "Weight Training"),
    ("FLEXIBILITY", "Flexibility"),
    ("ARMS", "Arms"),
    ("LEGS", "Legs"),
    ("BACK", "Back"),
    ("CORE", "Core"),
    ("CHEST", "Chest"),
)


class Profile(models.Model):
    profile = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, primary_key=True)
    points = models.IntegerField(default=0.0)
    
    def __str__(self):
        return self.profile.username
    
    def get_points(self):
        return points


class Exercise_Log(models.Model):
    exercise_type = models.CharField(max_length = 20, choices=exercises, default='Cardio')
    # region = models.CharField(max_length = 10, choices=muscle_regions, default='Arms')
    amount = models.DecimalField(max_digits = 4, decimal_places=2, default=0.0)
    date = models.DateField(default=datetime.date.today)
    profile = models.ForeignKey(Profile, null=True, related_name='logs', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)

class Goal_Log(models.Model):
    exercise_type = models.CharField(max_length=20, choices=exercises, default='Cardio')
    # region = models.CharField(max_length = 10, choices=muscle_regions, default='Arms')
    amount = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
    date = models.DateField(default=datetime.date.today)
    profile = models.ForeignKey(Profile, null=True, related_name='goals', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.exercise_type)

    def get_exercise_hours(self):
        total = 0
        for log in Exercise_Log.objects.all():
            if log.profile == self.profile and log.exercise_type == self.exercise_type and log.date >= self.date:
                total += log.amount
        return total


#class Points(models.Model):
#    amount = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
#    profile = models.OneToOneField(Profile, null=True, related_name='points', on_delete=models.CASCADE)

#    def get_points(self):
#        total = 0
#        for log in Exercise_Log.objects.all():
#            total += log.amount

#        self.amount = total
#        return total


# class Message(models.Model):
#     description = models.TextField()
#     pub_date = models.DateTimeField(auto_now_add=True)
#     author = models.CharField(max_length=200, null=False, default="no author")

#     class Meta:
#         ordering = ['pub_date']

#     def __str__(self):
#         return 'Comment {} by {}'.format(self.description, self.author)

class Group(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField()
    members = models.ManyToManyField(User, related_name="members")
    owner = models.ForeignKey(User, related_name="owner", on_delete = models.CASCADE)
    email = models.EmailField(max_length=200, null=True)
    private = models.BooleanField(default = False, null=False)
    # messages = models.ManyToManyField(Message, blank=True)


    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('group_detail', args=[str(self.id)])
    
class Message(models.Model):
    message = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='messages')
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, null=False, default="no author")

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return 'Comment {} by {}'.format(self.description, self.author)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    for user in User.objects.all():
        Profile.objects.get_or_create(profile=user)
