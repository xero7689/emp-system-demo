from django.shortcuts import render
from django.views import View

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from .forms import NewUserForm


@method_decorator(login_required, name='dispatch')
class PortalView(View):
    def get(self, request):
        return render(request, template_name="hr_system/portal.html")


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
                return render(request, template_name="hr_system/portal.html")
        messages.error(request, "Invalid username or password")


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
        messages.error(
            request, "Unsuccessful registration. Invalid information.")


class LogoutView(View):
    def get(self, request):
        return HttpResponse("Logout View")
