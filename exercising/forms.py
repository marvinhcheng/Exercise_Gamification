from django import forms

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