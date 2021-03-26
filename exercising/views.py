from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import User

class GoalsListView(generic.ListView):
    model = User
    template_name = 'exercising/goals.html'

class LogsListView(generic.ListView):
    model = User
    template_name = 'exercising/logs.html'