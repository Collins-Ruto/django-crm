from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "mb-4 shadow appearance-none border rounded py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "EmailAddress",
            }
        ),
    )
    first_name = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "mb-4 shadow appearance-none border rounded  py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "First Name",
            }
        ),
    )
    last_name = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "mb-4 shadow appearance-none border rounded  py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "Last Name",
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs[
            "class"
        ] = "mb-4 shadow appearance-none border rounded  py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["username"].label = ""
        self.fields[
            "username"
        ].help_text = '<span class="block text-xs"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields["password1"].widget.attrs[
            "class"
        ] = "mb-4 shadow appearance-none border rounded  py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields[
            "password1"
        ].help_text = '<span class="text-sm block"><small>Your password should: not similar to your personal information, 8+ characters, uncommon & not entirely numeric.</small></span>'

        self.fields["password2"].widget.attrs[
            "class"
        ] = "mb-4 shadow appearance-none border rounded  py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"
        self.fields["password2"].label = ""
        self.fields[
            "password2"
        ].help_text = '<span class="text-sm block"><small>Repeat the same password, for verification.</small></span>'

class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "mb-4 shadow appearance-none border rounded  py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "First Name",
            }
        ),
    )
    last_name = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "mb-4 shadow appearance-none border rounded  py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "Last Name",
            }
        ),
    )
    email = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "mb-4 shadow appearance-none border rounded  py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "Email Address",
            }
        ),
    )
    phone = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "mb-4 shadow appearance-none border rounded  py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "Phone",
            }
        ),
    )
    address = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "mb-4 shadow appearance-none border rounded  py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "Address",
            }
        ),
    )
    city = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "mb-4 shadow appearance-none border rounded  py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "City",
            }
        ),
    )
    state = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "mb-4 shadow appearance-none border rounded  py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "State",
            }
        ),
    )
    zipcode = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "mb-4 shadow appearance-none border rounded  py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "ZipCode",
            }
        ),
    )
    country = forms.CharField(
        label="",
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "class": "mb-4 shadow appearance-none border rounded  py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "Country",
            }
        ),
    )

    class Meta:
                model = Record
                exclude = ("user",)
                