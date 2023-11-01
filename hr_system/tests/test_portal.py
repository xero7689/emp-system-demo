from django.test import TestCase, Client
from django.urls import reverse
from hr_system.models import User, Employee, Role, Department


class LoginPortalTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpass'

        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        self.client = Client()

    def test_user_with_authenticated(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('portal_index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hr_system/portal.html')

    def test_user_without_authenticated(self):
        response = self.client.get(reverse('portal_index'))
        redirect_url = f'{reverse("portal_login")}?next={reverse("portal_index")}'
        self.assertRedirects(response, redirect_url, status_code=302,
                             target_status_code=200, msg_prefix="", fetch_redirect_response=True)

    def test_context_data_with_employee(self):
        role = Role.objects.create(
            title='Role', slug='role', description='Role Description', active=True)
        department = Department.objects.create(title='Department')
        employee = Employee.objects.create(user=self.user, role=role, department=department,
                                           date_of_hire='2022-01-01', service_status=Employee.ServiceStatus.AT_WORK)

        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('portal_index'))
        context = response.context

        self.assertEqual(context['user_data']['username'], 'testuser')
        self.assertEqual(context['employee_data']['id'], employee.id)
        self.assertEqual(context['service_status'], 'AT_WORK')
        self.assertEqual(context['department_data'].id, department.id)
        self.assertEqual(context['role_data'].id, role.id)

    def test_context_data_without_employee(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('portal_index'))
        context = response.context

        self.assertEqual(context['user_data']['username'], self.username)
        self.assertFalse('employee_data' in context)
        self.assertFalse('service_status' in context)
        self.assertFalse('department_data' in context)
        self.assertFalse('role_data' in context)
