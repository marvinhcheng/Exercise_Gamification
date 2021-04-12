from django import forms
from .models import Group, Message, exercises


class ExerciseForm(forms.Form):
    exercise_type = forms.MultipleChoiceField(choices = exercises, label ="Exercise Type")
    duration = forms.DecimalField(label = "Duration (in hours)")
    date = forms.DateField(label = "Date")


class GoalsForm(forms.Form):
    exercise_type = forms.MultipleChoiceField(choices = exercises, label ="Exercise Type")
    duration = forms.DecimalField(label = "Duration (in hours)")
    date = forms.DateField(label = "Date")


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields= ['name', 'description', 'private']


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['description']

class GroupAddForm(forms.Form):
    added_user = forms.CharField(label = "Enter a username to add to the group")

