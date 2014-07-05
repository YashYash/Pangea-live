from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

import requests
from django.shortcuts import render, redirect
from charity_app.forms import CharityForm
from charity_app.models import Video
from charity_app.models import Charity



@login_required
def charity_create(request, charity_id):
    charity = Charity.objects.get(id=charity_id)
    if request.method == "POST":
        charity_info = CharityForm(request.POST, instance=charity)
        if charity_info.is_valid():
            if charity_info.save():
                return redirect("charity_dashboard")
    else:
        charity_info = CharityForm(instance=charity)
    data = {'charity_info': charity_info, "charity": charity}
    return render(request, 'charity_home.html', data)


def charity_landing(request):
    return render(request, 'charity_landing.html')

@login_required
def charity_dashboard(request):
    charity = request.user.charity
    videos = Video.objects.filter(charity=3)
    data = {'charity': charity, "videos": videos}
    return render(request, 'charity_dashboard.html', data)

