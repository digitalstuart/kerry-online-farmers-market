from django.test import TestCase
from .forms import UserLoginForm


class UserLoginTest(TestCase):
    """Runs tests to check if user login form is working"""

    def test_valid_form(self):
        form = UserLoginForm(data={
            'username': 'admin',
            'password': 'testpassword1',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = UserLoginForm(data={
            'username': 'admin',
            'password': '',
        })
        self.assertFalse(form.is_valid())