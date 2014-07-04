from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

import requests
from django.shortcuts import render, redirect
from charity_app.forms import CharityForm
from charity_app.models import Video


def charity_landing(request):
    return render(request, 'charity_landing.html')

@login_required
def charity_create(request):
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


@login_required
def charity_dashboard(request):
    return render(request, 'charity_dashboard.html')