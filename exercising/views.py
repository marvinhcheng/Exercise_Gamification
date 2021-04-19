
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
import random
from django.utils import timezone
from .models import User, Exercise_Log, Profile, Goal_Log, Group, Message, exercises
from .forms import ExerciseForm, GoalsForm, GroupForm, MessageForm, GroupAddForm, EditGroupForm
from django.views.generic import TemplateView
from django.views.generic.list import View
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.core.exceptions import ObjectDoesNotExist

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
            # new_exercise.region_type = form.cleaned_data['region_type']
            new_exercise.amount = form.cleaned_data['amount']
            new_exercise.date = form.cleaned_data['date']
            new_exercise.profile = request.user.profile
            new_exercise.save()

            #This code mad me want to punch a hole through my screen
            if new_exercise.exercise_type[0] == 'CARDIO':
                if request.user.profile.points_cardio == None:
                    request.user.profile.points_cardio = 0
                    request.user.profile.points_total = 0
                request.user.profile.points_cardio += new_exercise.amount*16
                request.user.profile.points_total += new_exercise.amount*16
            if new_exercise.exercise_type[0] == 'WEIGHT_TRAINING':
                if request.user.profile.points_weight == None:
                    request.user.profile.points_weight = 0
                    request.user.profile.points_total = 0
                request.user.profile.points_weight += new_exercise.amount*30
                request.user.profile.points_total += new_exercise.amount*30
            if new_exercise.exercise_type[0] == 'CALISTHENICS':
                if request.user.profile.points_calis == None:
                    request.user.profile.points_calis = 0
                    request.user.profile.points_total = 0
                request.user.profile.points_calis += new_exercise.amount*8
                request.user.profile.points_total += new_exercise.amount*8

            request.user.profile.logs.add(new_exercise)
            request.user.save()
            request.user.profile.save()

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
            # new_goal.region_type = form.cleaned_data['region_type']
            new_goal.amount = form2.cleaned_data['amount']
            new_goal.profile = request.user.profile
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

class CreateGroup(TemplateView):
    template_name = 'exercising/makegroup.html'
    def post(self, request):
        group_form = GroupForm(request.POST)
        if group_form.is_valid():
            group = group_form.save(commit=False)
            group.owner = request.user
            group.pub_date = timezone.localtime()
            group.email = request.user.email
            group.save()
            group.members.add(group.owner)
        context = {'group_form': group_form}
        return redirect('/groups/')
    
    def get(self, request):
        group_form = GroupForm()
        return render(request, self.template_name, {'group_form': group_form})

# def edit_group(request, group_id):
#     template_name = 'exercising/editgroup.html'
#     # group = Group.objects.get(id=group_id)
#     if request.method == "POST":
#         edit_form = EditGroupForm(request.POST)
#         if edit_form.is_valid():
#             group = edit_form.save(commit=False)
#             group.owner = request.user
#             # group.pub_date = group.pub_date
#             group.pub_date = timezone.localtime()
#             group.email = request.user.email
#             edit_form.save()
#             return HttpResponseRedirect('/groups/'+str(group_id))
#     else:
#         edit_form = EditGroupForm()
#     return render(request, template_name, {'edit_form': edit_form})

class edit_group(TemplateView):
    template_name = 'exercising/editgroup.html'
    model = Group
    form_class = EditGroupForm

    def get(self, request, group_id):
        group = Group.objects.get(id=group_id)
        edit_form = EditGroupForm(instance=group)
        context = {'edit_form':edit_form, 'group': group}
        return render(request, self.template_name, context)
    
    def post(self, request, group_id):
        group = Group.objects.get(id=group_id)
        edit_form = EditGroupForm(request.POST, request.FILES, instance = group)
        if edit_form.is_valid():
            group = edit_form.save(commit=False)
            group.owner = request.user
            group.pub_date = group.pub_date
            # group.pub_date = timezone.localtime()
            group.email = request.user.email
            group.save()
            group.save()
            edit_form.save()
            return HttpResponseRedirect('/groups/'+str(group_id))

def delete_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.delete()
    return redirect('/groups/')



class GroupListView(generic.ListView):
    model = Message
    template_name = 'exercising/group.html'
    def get_queryset(self):
        return Group.objects.all()



def group_detail(request, group_id):
    template_name = 'exercising/details.html'
    group = Group.objects.get(id=group_id)
    
    new_message = None
   
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            new_message = message_form.save(commit=False)
            new_message.author = request.user
            new_message.pub_date = timezone.localtime()
            new_message.message_id = group_id
            new_message.save()
    else:
        message_form = MessageForm()
    
    messages = group.messages.all()
    context = {
        'group' : group,
        'messages' : messages,
        'new_message':new_message,
        'message_form' : message_form
    }

    return render(request, template_name, context)


def add_to_group(request, group_id):
    template_name = 'exercising/add_user.html'
    group = Group.objects.get(id=group_id)
    if request.method == "POST":
        add_form = GroupAddForm(request.POST)
        if add_form.is_valid():
            try:
                addee = User.objects.get(username = add_form.cleaned_data['added_user'])
                group.members.add(addee)
                
                
            except ObjectDoesNotExist:
                return HttpResponse('Account with username does not exist')
            return HttpResponseRedirect('/groups/'+str(group_id))
    else:
        add_form = GroupAddForm()
    
    return render(request, template_name, {'add_form': add_form})


    
def join_group(request, group_id):
    user = request.user
    group = Group.objects.filter(id=group_id).first()
    already_member = False

    for member in group.members.all():
        if (user == member):
            already_member = True
    if (not already_member):
        group.members.add(user)
    else:
        group.members.remove(user)
        return redirect('/groups/')

    return redirect('/groups/'+str(group_id))