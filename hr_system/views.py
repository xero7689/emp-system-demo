from django.shortcuts import render
from django.views import View

from django.http import HttpResponse

class PortalView(View):
    def get(self, request):
        return HttpResponse("Portal View")


class LoginView(View):
    def get(self, request):
        return HttpResponse("Login View")


class RegisterView(View):
    def get(self, request):
        return HttpResponse("Register View")


class LogoutView(View):
    def get(self, request):
        return HttpResponse("Logout View")
