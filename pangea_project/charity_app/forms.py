from django.forms import ModelForm
from charity_app.models import Charity
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

__author__ = 'yash'

class CharityForm(ModelForm):
    class Meta:
        model = Charity
        exclude = ["user"]






