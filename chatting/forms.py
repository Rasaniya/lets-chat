from django import forms
from django.forms import ModelForm
from .models import *

class TextForm(forms.ModelForm):
    name = forms.CharField()
    message = forms.CharField()

    class Meta:
        model = Text
        fields='__all__'
