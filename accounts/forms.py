from django import forms
from django.contrib.auth.models import User, auth
from .models import UserInfo


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ()

class NewDriver(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ('PhoneNumber','AutoModel','CarNumber','CarImage',)