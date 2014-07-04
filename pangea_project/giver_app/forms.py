from django.forms import ModelForm
from giver_app.models import Giver
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

__author__ = 'aakash'

class GiverForm(ModelForm):
    class Meta:
        model = Giver
        exclude = ["user"]