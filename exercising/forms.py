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
    current_weight = forms.DecimalField(label = "Current weight")
    current_date = forms.DateField(label = "Today's Date")

    future_weight = forms.DecimalField(label = "Goal weight")
    future_date = forms.DateField(label = "Goal day to complete weight loss by")


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
    #Add way to count times an exercise was done in a week