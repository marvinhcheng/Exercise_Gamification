from django.test import Client, TestCase
from http import HTTPStatus
from django.contrib.auth.models import User

from exercising.models import Exercise_Log
from exercising.forms import ExerciseForm

# Create your tests here.
class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'mhc9yq',
            'password': 'B0ttle123!'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

class logsTest(TestCase):
    # def test_form_post(self):
    #     self.client.force_login(User.objects.get_or_create(username='testuser')[0])
    #     response = self.client.post('/logs/', data = {'exercise_type': ("Cardio", "Cardio"), 'duration': '1.0', 'date': '04/04/2021'})
    #     self.assertEqual(response.status_code, 302)     #302 redirects to home page
    #     #self.assertContains(response, "2021-04-04")

    # def test_form_success(self):
    #     form_data = {'exercise_type': ("Cardio", "Cardio"),
    #                  'duration': '1.0',
    #                  'date': '04/04/2021'}

    #     form = ExerciseForm(data = form_data)
    #     self.assertTrue(form.is_valid())

    def test_form_invalid_input(self):
        form_data = {'exercise_type': ("Fart", "Fart"),
                     'duration': '123.0',
                     'date': '04/04/2021'}

        form = ExerciseForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_form_no_input(self):
        form_data = {'exercise_type': ("", ""),
                     'duration': '',
                     'date': ''}

        form = ExerciseForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_form_no_date(self):
        form_data = {'exercise_type': ("Cardio", "Cardio"),
                     'duration': '1.00',
                     'date': ''}

        form = ExerciseForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_form_no_duration(self):
        form_data = {'exercise_type': ("Cardio", "Cardio"),
                     'duration': '1.00',
                     'date': ''}

        form = ExerciseForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_form_no_exercise(self):
        form_data = {'exercise_type': ("",""),
                     'duration': '1.00',
                     'date': ''}

        form = ExerciseForm(data = form_data)
        self.assertFalse(form.is_valid())


