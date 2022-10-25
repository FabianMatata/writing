from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Assignment, GENDER_OPTIONS
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from crispy_forms.bootstrap import InlineRadios, FormActions

from crispy_forms.layout import Submit

from .models import Candidates

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

# class UniversityForm(forms.Form): 

#     SUBJECT_CHOICES = (
#         (1, 'web development'),
#         (2, 'systems programming'),
#         (3, 'data science'),
#     )

#     name = forms.CharField()
#     age = forms.IntegerField()
#     subject = forms.ChoiceField(choices=SUBJECT_CHOICES)
#     date_of_birth = forms.DateField()


class AssignmentForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_OPTIONS,
                            widget=forms.RadioSelect,
                            initial='male')
    class Meta:
        model = Assignment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # self.helper.add_input(Submit('save_assignment', 'Save Assignment'))
        # self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn btn-danger'))

        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('email')
            ),
            InlineRadios('gender'),
            'city',
            FormActions(
                Submit('save_assignment', 'Save Assignment')
            )
        )


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidates
        fields = ('name', 'phone', 'email','gender','career')
        labels = {
            'name':'Name',
            'email':'Email',
        }
        #Placeholder
        widget = {
            'name':forms.TimeInput(attrs={'placeholder':'Your name'}),
            'phone':forms.TimeInput(attrs={'placeholder':'Your phone'}),
            'email':forms.TimeInput(attrs={'placeholder':'Your email'}),
        }

    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)
        self.fields['gender'].choices = [("", "Select a gender"),] + list(self.fields['gender'].choices)[1:]
        self.fields['career'].empty_label = "Select an option"
        self.fields['email'].required = True

