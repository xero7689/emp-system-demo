from django.test import TestCase, Client
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from hr_system.models import User


class LoginViewTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpass'

        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        self.client = Client()

    def test_get(self):
        response = self.client.get(reverse('portal_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hr_system/login.html')
        self.assertIsInstance(
            response.context['login_form'], AuthenticationForm)

    def test_post_valid_credentials(self):
        response = self.client.post(reverse('portal_login'), data={
                                    'username': self.username, 'password': self.password})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('portal_index'))

    def test_post_invalid_credentials(self):
        response = self.client.post(reverse('portal_login'), data={
                                    'username': self.username, 'password': 'invalid_password'})
        self.assertEqual(response.status_code, 401)
        self.assertTemplateUsed(response, 'hr_system/login.html')
        self.assertIsInstance(
            response.context['login_form'], AuthenticationForm)
