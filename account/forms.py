from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form): 
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm): 
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta: 
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_employee', 'is_customer')

class UniversityForm(forms.Form): 

    SUBJECT_CHOICES = (
        (1, 'web development'),
        (2, 'systems programming'),
        (3, 'data science'),
    )

    name = forms.CharField()
    age = forms.IntegerField()
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
    date_of_birth = forms.DateField()
