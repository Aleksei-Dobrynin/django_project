from django import forms
from django.contrib.auth.models import User, auth


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ()