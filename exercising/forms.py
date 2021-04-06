from django import forms
from .models import Group


class ExerciseForm(forms.Form):
    exercises = (
        ("Cardio", "Cardio"),
        ("Arms", "Arms"),
        ("Legs", "Legs"),
        ("Back", "Back"),
        ("Core", "Core"),
        ("Chest", "Chest"),
        ("Flexibility", "Flexibility")
    )
    exercise_type = forms.MultipleChoiceField(choices = exercises, label ="Exercise Type")
    duration = forms.DecimalField(label = "Duration (in hours)")
    date = forms.DateField(label = "Date")

class GoalsForm(forms.Form):
    exercises = (
        ("Cardio", "Cardio"),
        ("Arms", "Arms"),
        ("Legs", "Legs"),
        ("Back", "Back"),
        ("Core", "Core"),
        ("Chest", "Chest"),
        ("Flexibility", "Flexibility")
    )
    exercise_type = forms.MultipleChoiceField(choices = exercises, label ="Exercise Type")
    duration = forms.DecimalField(label = "Duration (in hours)")


class GroupForm(forms.ModelForm):
    # fields= "__all__"
    # exclude = ['email']

    class Meta:
        model = Group
        fields= ['name', 'description']

