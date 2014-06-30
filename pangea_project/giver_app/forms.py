from django.forms import ModelForm
from giver_app.models import Giver
from django import forms
from django.forms import ModelForm

__author__ = 'aakash'

class GiverForm(ModelForm):
    class Meta:
        model = Giver