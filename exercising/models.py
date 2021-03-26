import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    firstName = models.CharField(max_length = 200)
    lastName = models.CharField(max_length = 200)
    identification = models.CharField(max_length = 200)
    score = models.CharField(max_length = 200)

    def __str__(self):
        return self.text