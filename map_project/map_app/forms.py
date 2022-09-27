from django import forms
from .models import Priority

class AuthForm(forms.Form):
    username = forms.CharField(max_length=12, label="Username")
    password = forms.CharField(max_length=12, label="Password", widget=forms.PasswordInput)


class EventForm(forms.Form):
    title = forms.CharField(max_length=100, label="Title")
    description = forms.CharField(max_length=100, label="Description")
    location = forms.CharField(max_length=100, label="Location")
    date_start = forms.DateField(label="Start Date")
    date_end = forms.DateField(label="End Date")