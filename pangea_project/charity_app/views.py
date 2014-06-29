from django.shortcuts import render

# Create your views here.

import requests
from django.shortcuts import render, redirect
from charity_app.forms import CharityForm


def charity_home(request):
    if request.method == "POST":
        charity_info = CharityForm(request.POST)
        if charity_info.is_valid():
            charity = charity_info.save(commit=False)
            charity.save()
            return redirect("charity_home")
    else:
        charity_info = CharityForm()
    data = {'charity_info': charity_info}
    return render(request, 'charity_home.html', data)

