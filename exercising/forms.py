from django import forms
from .models import Group, Message, Exercise_Log, Goal_Log, exercises#, regions


class ExerciseForm(forms.Form):
    exercise_type = forms.MultipleChoiceField(choices = exercises, label="Exercise Type")
    # region_type = forms.MultipleChoiceField(choices=regions, label="Muscle Region")
    amount = forms.IntegerField(label="Duration (min)")
    # if exercise_type == "Weight Training":
    #     amount.label = "Number of Reps"
    # else:
    #     amount.label = "Duration (min)"
    
    date = forms.DateField(label="Date")


class GoalsForm(forms.Form):
    exercise_type = forms.MultipleChoiceField(choices=exercises, label="Exercise Type")
    # region_type = forms.MultipleChoiceField(choices=regions, label="Muscle Region")
    amount = forms.IntegerField(label="Duration (min)")
    # if exercise_type == "Weight Training":
    #     amount.label = "Number of Reps"
    # else:
    #     amount.label = "Duration (min)"
    date = forms.DateField(label="Date")


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields= ['name', 'description', 'private']

class EditGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields= ['name', 'description', 'private']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['description']

class GroupAddForm(forms.Form):
    added_user = forms.CharField(label ="Enter a username to add to the group")

