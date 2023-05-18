from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': '', 'placeholder': 'EmailAddress'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': '', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': '', 'placeholder': 'Last Name'}))

    # def __init__(self, *args):
    #     super(SignUpForm, self).__init__(*args))
        