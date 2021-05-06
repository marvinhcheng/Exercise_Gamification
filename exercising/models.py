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
    ("CALISTHENICS", "Calisthenics"),
)

# regions = (
#     ("ANY", "Any"),
#     ("ARMS", "Arms"),
#     ("LEGS", "Legs"),
#     ("BACK", "Back"),
#     ("CORE", "Core"),
#     ("CHEST", "Chest"),
# )


class Profile(models.Model):
    profile = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, primary_key=True)
    points_cardio = models.IntegerField(default=0, null=True)
    points_weight = models.IntegerField(default=0, null=True)
    points_calis = models.IntegerField( default=0, null=True)
    points_total = models.IntegerField(default=0)
    
    def __str__(self):
        return self.profile.username

    def get_total_level(self):
        return int((self.points_total/1000)+1)

    def get_cardio_level(self):
        return int((self.points_cardio/1000)+1)

    def get_weight_level(self):
        return int((self.points_weight/1000)+1)
    
    def get_calis_level(self):
        return int((self.points_calis/1000)+1)

    def get_points_left(self):
        return 1000 - int(self.points_total % 1000)

    def get_cardio_left(self):
        return 1000 - int(self.points_cardio % 1000)
        
    def get_weight_left(self):
        return 1000 - int(self.points_weight % 1000)
    
    def get_calis_left(self):
        return 1000 - int(self.points_calis % 1000)

    def get_level_progress(self):
        return 100 - round(((1000 - int(self.points_total % 1000))/ 1000 * 100),2)
    
    def get_cardio_progress(self):
        return 100 - round(((1000 - int(self.points_cardio % 1000))/ 1000 * 100),2)
    
    def get_weight_progress(self):
        return 100 -round(((1000 - int(self.points_weight % 1000))/ 1000 * 100),2)
    
    def get_calis_progress(self):
        return 100 -round(((1000 - int(self.points_calis % 1000))/ 1000 * 100),2)

class Exercise_Log(models.Model):
    exercise_type = models.CharField(max_length = 20, choices=exercises, default='Cardio')
    # region_type = models.CharField(max_length = 10, choices=regions, default='Any')
    amount = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today)
    profile = models.ForeignKey(Profile, null=True, related_name='logs', on_delete=models.CASCADE)

    def get_points(self):
        if(self.exercise_type == 'CARDIO'):
            return self.amount * 16
        elif(self.exercise_type == 'CALISTHENICS'):
            return self.amount * 8
        elif(self.exercise_type == "WEIGHT_TRAINING"):
            return self.amount * 30

    def __str__(self):
        return str(self.date)

class Goal_Log(models.Model):
    exercise_type = models.CharField(max_length=20, choices=exercises, default='Cardio')
    # region_type = models.CharField(max_length = 10, choices=regions, default='Any')
    amount = models.IntegerField(default=0)
    date = models.DateField(default=datetime.date.today)
    profile = models.ForeignKey(Profile, null=True, related_name='goals', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.exercise_type)

    def get_exercise_amount(self):
        total = 0
        for log in Exercise_Log.objects.filter(profile=self.profile, exercise_type=self.exercise_type):
            if log.date >= self.date:
                # if log.region_type == "Any":
                total += log.amount
                # else: 
                #     if log.region_type == self.region_type:
                #         total += log.amount
        if total >= self.amount:
            return self.amount
        return total
    
    def get_progress(self):
        # progress = self.amount
        # return progress
        total = 0
        for log in Exercise_Log.objects.filter(profile=self.profile, exercise_type=self.exercise_type):
            if log.date >= self.date:
                # if log.region_type == "Any":
                total += log.amount
                # else: 
                #     if log.region_type == self.region_type:
                #         total += log.amount
        if total >= self.amount:
            return 100
        return round((total / self.amount * 100),2)


class Group(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField()
    members = models.ManyToManyField(User, related_name="members")
    owner = models.ForeignKey(User, related_name="owner", on_delete = models.CASCADE)
    email = models.EmailField(max_length=200, null=True)
    private = models.BooleanField(default = False, null=False)


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
