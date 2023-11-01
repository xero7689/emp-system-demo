from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from .models import User, Employee, Role, Department
from .forms import NewUserForm


@method_decorator(login_required, name='dispatch')
class PortalView(TemplateView):
    template_name = 'hr_system/portal.html'

    def get(self, request):
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(pk=self.request.user.id)
        employee = Employee.objects.select_related(
            'department').select_related('role').filter(user=user).first()

        if employee:
            service_status = Employee.ServiceStatus(
                employee.service_status).name
            department_data = Department.objects.get(pk=employee.department_id)
            role_data = Role.objects.get(pk=employee.role_id)

            context['employee_data'] = employee.__dict__
            context['service_status'] = service_status
            context['department_data'] = department_data
            context['role_data'] = role_data

        context['user_data'] = user.__dict__

        return context


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("portal_index"))

        form = AuthenticationForm()
        return render(request, template_name="hr_system/login.html", context={"login_form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You're now logged in as {username}.")
                return HttpResponseRedirect(reverse("portal_index"))

        messages.error(request, "Invalid username or password")
        response = render(
            request, template_name="hr_system/login.html", context={"login_form": form})
        response.status_code = 401
        return response


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("portal_index"))

        form = NewUserForm()
        return render(request, template_name="hr_system/register.html", context={"register_form": form})

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('portal_index'))
        else:
            messages.error(
                request, "Unsuccessful registration. Invalid information.")

            response = render(
                request, template_name="hr_system/register.html", context={"register_form": form})
            response.status_code = 422
            return response


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out.")
        return HttpResponseRedirect(reverse("portal_index"))
