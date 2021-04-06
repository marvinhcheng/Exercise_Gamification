
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import User, Exercise_Log, Profile, Goal_Log, Group, Message
from .forms import ExerciseForm, GoalsForm, GroupForm
from django.views.generic import TemplateView

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
    model = Group
    template_name = 'exercising/grouplist.html'
    def get_queryset(self):
        return Group.objects.all()
    


# def group_detail(request, pk):
#     # template_name = 'exercising/details.html'
#     # group = Group.objects.get(id=owner_id)
#     # return render(request, template_name)

#     return render(request, 'detail.html',{
#         'group' : get_object_or_404(Group, pk=id)
#     })


class group_detail(generic.DetailView):
    model = Group
    template_name = 'exercising/details.html'

    

            
