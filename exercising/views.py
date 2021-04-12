from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
import random
from django.utils import timezone
from .models import User, Exercise_Log, Profile, Goal_Log
from .forms import ExerciseForm, GoalsForm
from django.views.generic import TemplateView
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class GoalsListView(generic.ListView):
    model = Profile
    template_name = 'exercising/goals.html'

class LogsListView(generic.ListView):
    model = Profile
    template_name = 'exercising/logs.html'
    # context_object_name = 'logs_list'

    # def get_queryset(self):
    # #     return Profile.logs.objects.order_by('-logs.date')
    #     return Profile.logs.objects.all()

def add_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            new_exercise = Exercise_Log()
            new_exercise.exercise_type = form.cleaned_data['exercise_type']
            new_exercise.duration = form.cleaned_data['duration']
            new_exercise.date = form.cleaned_data['date']
            new_exercise.save()

            request.user.profile.logs.add(new_exercise)
            request.user.save()
            return HttpResponseRedirect('/logs/')
    else:
        form = ExerciseForm()
    return render(request, 'exercising/logs.html', {'form': form})

def add_goal(request):
    if request.method == 'POST':
        form2 = GoalsForm(request.POST)
        if form2.is_valid():
            new_goal = Goal_Log()
            new_goal.exercise_type = form2.cleaned_data['exercise_type']
            new_goal.duration = form2.cleaned_data['duration']
            new_goal.save()

            request.user.profile.goals.add(new_goal)
            request.user.save()
            return HttpResponseRedirect('/goals/')
    else:
        form2 = GoalsForm()
    return render(request, 'exercising/goals.html', {'form': form2})

def map(request):
    mapbox_access_token = 'pk.eyJ1Ijoic2VyaGlpMDQ0IiwiYSI6ImNrbmR0d281ZTBhdXgyem9kdDJnNHdtdmcifQ.8K3hi5bBXp2lZTwOWvbFUA'
    return render(request, 'exercising/map.html', {'mapbox_access_token': mapbox_access_token})

def music (request):
    artists = [
        'https://open.spotify.com/artist/791L9eOcjQ3FiorSX2xvcf?si=YYpeZft2RsKDWG_TfGfDBQ',
        'https://open.spotify.com/artist/3QYk6NujwZNNXFciGYfo0U?si=S29foxTySAqbkIoRFb5AhA',
        'https://open.spotify.com/artist/5F4tRDDqkTLhPUb0bVceWQ?si=H2mY8j6yQ2y6OJ4elsTzoQ',
        'https://open.spotify.com/artist/6dJnCgWrQmJNAnmdzQi2Vi?si=AVjoEn-dQDqHcPbCzqGHsw',
        'https://open.spotify.com/artist/44YvYIWPDPNLJaHiHktrJD?si=mMWTjWK6She9payvsuTMXg'
    ]
    x = random.randint(0, 4)
    # if request.method == 'POST':
    # artist_uri = request.POST.get('uri')
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='f3195ba0f7ec40d9981e81d14d69192f',client_secret='f704f87a345a4a919aa2f167e97739cf'))
    results = spotify.artist_top_tracks(artists[x])
    final_result = results['tracks'][:10]
    return render(request, 'exercising/music.html', {"results": final_result})
    # else:
    #     # for track in results['tracks'][:10]:
    #     #     print('track    : ' + track['name'])
    #     #     print('audio    : ' + track['preview_url'])
    #     #     print('cover art: ' + track['album']['images'][0]['url'])
    #     #     print()
    #     return render(request, 'exercising/music.html', )
