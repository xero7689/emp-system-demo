from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1",
                  "password2", "phone_number", "address")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
