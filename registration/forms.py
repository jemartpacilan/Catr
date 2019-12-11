from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from .models import Caterer, Consumer


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    def login_user(self):
        pass


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class CatererSignUpForm(forms.ModelForm):
    class Meta:
        model = Caterer
        fields = ('profile_image', 'business_name', 'business_description',
                  'province_address', 'municipality_address', 'street_address',
                  'zip_code')


class ConsumerSignUpForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ('profile_image', )


class TestUploadForm(forms.Form):
    image_name = forms.CharField(max_length=100)
    image_binary = forms.ImageField()
