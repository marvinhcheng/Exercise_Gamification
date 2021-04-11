
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import User, Exercise_Log, Profile, Goal_Log, Group, Message
from .forms import ExerciseForm, GoalsForm, GroupForm, MessageForm, GroupAddForm
from django.views.generic import TemplateView
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
        context = {'group_form': group_form}
        return redirect('/groups/')
    
    def get(self, request):
        group_form = GroupForm()
        return render(request, self.template_name, {'group_form': group_form})

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

    # if request.method == 'POST':
    #     add_form = GroupAddForm(request.POST)
    #     if add_form.is_valid():
    #         addee = User.objects.get(username = add_form.cleaned_data['added_user'])
    #         group.members.add(addee)
    # else:
    #     add_from = GroupAddForm()
    # context = {
    #     'group' : group,
    #     'add_form': add_form
    # }
    # return render(request, template_name, context)

    
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







    

            
