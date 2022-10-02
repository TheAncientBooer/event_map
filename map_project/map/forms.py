from django import forms
from .models import Event
from django.forms import ModelForm

class EventForm(forms.ModelForm):
    #address = forms.CharField(label='address')
    class Meta:
        model = Event
        fields = '__all__'