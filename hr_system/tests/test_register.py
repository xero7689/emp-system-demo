from django.contrib.messages import get_messages

from django.test import TestCase, Client
from django.urls import reverse

from hr_system.models import User
from hr_system.forms import NewUserForm


class RegisterViewTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpass'

        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        self.client = Client()

    def test_user_with_authenticated(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('portal_register'))

        redirect_url = f'{reverse("portal_index")}'
        self.assertRedirects(response, redirect_url, status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_user_without_authenticated(self):
        response = self.client.get(reverse('portal_register'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hr_system/register.html')
        self.assertIsInstance(
            response.context['register_form'], NewUserForm)

    def test_post_valid_form(self):
        post_data = {
            'username': 'testuser2',
            'email': 'testuser2@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'phone_number': '1234567890',
            'address': 'Test Address'
        }

        response = self.client.post(reverse('portal_register'), data=post_data)
        self.assertRedirects(response, reverse('portal_index'), status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)

        exists = User.objects.filter(
            username=post_data['username'], email=post_data['email'])
        self.assertTrue(exists)

    def test_post_invalid_form(self):
        post_data = {
            'username': 'testuser2',
            'email': 'testuser2@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'phone_number': '1234567890',
            'address2': 'Test Address',
        }
        response = self.client.post(reverse('portal_register'), data=post_data)

        self.assertEqual(response.status_code, 422)
        self.assertTemplateUsed(response, 'hr_system/register.html')

        self.assertIsInstance(
            response.context['register_form'], NewUserForm)
