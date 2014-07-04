from django.shortcuts import render
from django.shortcuts import render, redirect
from giver_app.forms import GiverForm
from giver_app.models import Giver
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def giver_create(request, giver_id):
    giver = Giver.objects.get(id=giver_id)
    if request.method == "POST":
        giver_info = GiverForm(request.POST, instance=giver)
        if giver_info.is_valid():
            if giver_info.save():
                return redirect("charity_dashboard")
    else:
        giver_info = GiverForm(instance=giver)
    data = {'giver_info': giver_info, "giver": giver}
    return render(request, 'giver_home.html', data)

def giver_landing(request):
    return render(request, 'giver_landing.html')

@login_required
def giver_dashboard(request):
    giver = request.user.giver
    data = {"giver":giver}
    return render(request, 'giver_dashboard.html', data)


