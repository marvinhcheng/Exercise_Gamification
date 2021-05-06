from django.test import Client, TestCase
from http import HTTPStatus
from django.contrib.auth.models import User
from django.utils import timezone

from exercising.models import Exercise_Log, Goal_Log, Group, Message
from exercising.forms import ExerciseForm, GoalsForm, GroupForm, EditGroupForm, MessageForm

# Create your tests here.
# https://docs.djangoproject.com/en/3.2/topics/testing/overview/
class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'bsa2up',
            'password': 'b04E20n01'}
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

    def test_form_success(self):
        form_data = {'exercise_type': "CARDIO",
                     'amount': '10',
                     'date': '04/04/2021'}

        form = ExerciseForm(data = form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_input(self):
        form_data = {'exercise_type': "Fart",
                     'amount': '123.0',
                     'date': '04/04/2021'}

        form = ExerciseForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_input(self):
        form_data = {'exercise_type': "CARDIO",
                     'amount': '-10',
                     'date': '04/04/2021'}

        form = ExerciseForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_form_no_input(self):
        form_data = {'exercise_type': "",
                     'amount': '',
                     'date': ''}

        form = ExerciseForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_form_no_date(self):
        form_data = {'exercise_type': "CARDIO",
                     'duration': '1',
                     'date': ''}

        form = ExerciseForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_form_no_duration(self):
        form_data = {'exercise_type': "CARDIO",
                     'duration': '1',
                     'date': ''}

        form = ExerciseForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_form_no_exercise(self):
        form_data = {'exercise_type': "",
                     'duration': '1',
                     'date': ''}

        form = ExerciseForm(data = form_data)
        self.assertFalse(form.is_valid())

class goalsTest(TestCase):

    def test_form_success(self):
        form_data = {'exercise_type': "CARDIO",
                     'amount': '10',
                     'date': '04/04/2021'}

        form = GoalsForm(data = form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_input(self):
        form_data = {'exercise_type': "Fart",
                     'amount': '123.0',
                     'date': '04/04/2021'}

        form = GoalsForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_form_invalid_input(self):
        form_data = {'exercise_type': "CARDIO",
                     'amount': '-10',
                     'date': '04/04/2021'}

        form = GoalsForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_form_no_input(self):
        form_data = {'exercise_type': "",
                     'amount': '',
                     'date': ''}

        form = GoalsForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_form_no_date(self):
        form_data = {'exercise_type': "CARDIO",
                     'duration': '1',
                     'date': ''}

        form = GoalsForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_form_no_duration(self):
        form_data = {'exercise_type': "CARDIO",
                     'duration': '1',
                     'date': ''}

        form = GoalsForm(data = form_data)
        self.assertFalse(form.is_valid())

    def test_form_no_exercise(self):
        form_data = {'exercise_type': "",
                     'duration': '1',
                     'date': ''}

        form = GoalsForm(data = form_data)
        self.assertFalse(form.is_valid())


class groupTest(TestCase):
    def setup(self):
        user = User.objects.create_user(
            username = 'example',
            password = 'examplepass',
            email = 'example@example.com'
        )
        group = Group.objects.create(
            name='group_name',
            description = 'this is a description',
            pub_date = timezone.now(),
            email = user.email,
            owner = user,
            private = True
        )
        return group

    def test_valid_form(self):
        group = self.setup()
        form_data = {
            'name': group.name,
            'description': group.description,
            'private': group.private
        }
        form = GroupForm(data=form_data)
        self.assertTrue(form.is_valid())


    def test_invalid_form(self):
        form_data = {
            'name': '',
            'description': 'this is a description',
            'private': 'True'
        }
        form = GroupForm(data=form_data)
        self.assertFalse(form.is_valid())

    """
    Title: How do I test Django QuerySets are equal
    Date: 5/5/21
    url https://stackoverflow.com/questions/17685023/how-do-i-test-django-querysets-are-equal
    """
    def test_add_remove_user(self):
        group = self.setup()
        addee = User.objects.create_user(
            username = 'ex',
            password = 'expass',
            email = 'ex@example.com'
        )
        group.members.add(addee)
        self.assertQuerysetEqual(group.members.all(), ["<User: ex>"])
        group.members.remove(addee)
        self.assertQuerysetEqual(group.members.all(), [])

 


class editGroupTest(TestCase):
    def setup(self):
        user = User.objects.create_user(
            username = 'example',
            password = 'examplepass',
            email = 'example@example.com'
        )
        group = Group.objects.create(
            name='group_name',
            description = 'this is a description',
            pub_date = timezone.now(),
            email = user.email,
            owner = user,
            private = True
        )
        return group
    
    def test_valid_form(self):
        form_data = {
            'name': 'Ben',
            'description': 'this is a description',
            'private': 'False'
        }
        form = EditGroupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_no_name_form(self):
        form_data = {
            'name': '',
            'description': 'this is a description',
            'private': 'True'
        }
        form = EditGroupForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_no_desc_form(self):
        form_data = {
            'name': 'name',
            'description': '',
            'private': 'False'
        }
        form = EditGroupForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_delete_group(self):
        group = self.setup()
        self.assertQuerysetEqual(Group.objects.all(), ["<Group: group_name>"])
        group.delete()
        self.assertQuerysetEqual(Group.objects.all(), [])

class messageTest(TestCase):
    def setup(self):
        user = User.objects.create_user(
            username = 'example',
            password = 'examplepass',
            email = 'example@example.com'
        )
        group = Group.objects.create(
            name='group_name',
            description = 'this is a description',
            pub_date = timezone.now(),
            email = user.email,
            owner = user,
            private = True
        )
        message = Message.objects.create(
            message = group,
            author = user,
            description = 'this is a message',
            pub_date = timezone.now()
        )
        return message
    def test_valid_message(self):
        message = self.setup()
        form_data = {
            'description': message.description
        }
        form = MessageForm(data=form_data)
        self.assertTrue(form.is_valid())
    def test_invalid_message(self):
        message = self.setup()
        form_data = {
            'description': ""
        }
        form = MessageForm(data=form_data)
        self.assertFalse(form.is_valid())

    
