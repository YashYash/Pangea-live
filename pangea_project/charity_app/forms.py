from django.forms import ModelForm
from charity_app.models import Charity
from django import forms
from django.forms import ModelForm

__author__ = 'yash'

class CharityForm(ModelForm):
    class Meta:
        model = Charity






