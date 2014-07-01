from django.shortcuts import render
from django.shortcuts import render, redirect
from giver_app.forms import GiverForm
from giver_app.models import Giver
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def giver_create(request):
    if request.method == 'POST':
        giver_info = GiverForm(request.POST)
        if giver_info.isValid():
            giver = giver_info.save(commit=false)
            giver.save()
            return redirect("giver_home")
    else:
        giver_info = GiverForm()
    activeuser = request.user.activeuser
    data = {'giver_info': giver_info, 'activeuser': activeuser}
    return render(request, 'giver_home.html', data)

def giver_landing(request):
    return render(request, 'giver_landing.html')