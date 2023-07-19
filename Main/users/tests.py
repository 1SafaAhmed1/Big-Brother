from django.contrib.auth import get_user_model
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve, reverse_lazy

from .forms import ProfileCreationForm
from .views import RegistrationView

# Create your tests here.


class SignupPageTests(TestCase, SimpleTestCase):

    # Set up to initialize test data before running unit tests
    def setUp(self):
        url = reverse('registration')
        self.response = self.client.get(url)
        self.username = 'testuser'
        self.university = 'northsouth'
        self.first_name = 'test'
        self.last_name = 'user'
        self.password = 'qwerty@1234'


    # Unit test to check if registration page shows the correct template
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/registration.html')
        self.assertContains(self.response, 'Sign Up')


    # Unit test to check if registration form displays the correct form
    def test_signup_form(self):
        form = self.response.context.get('form')
        response = self.client.post(reverse('registration'), {
            'username': self.username,
            'university': self.university,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password1': self.password,
            'password2': self.password,
        })
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(form, ProfileCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')


    # Unit test to check if registration view works as intended
    def test_signup_view(self):
        view = resolve('/users/registration/')
        self.assertEqual(
            view.func.__name__,
            RegistrationView.as_view().__name__
        )