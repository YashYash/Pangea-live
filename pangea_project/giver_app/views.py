from django.shortcuts import render
from django.shortcuts import render, redirect
from giver_app.forms import GiverForm
from giver_app.models import Giver
# Create your views here.


def giver_home(request):
    if request.method == 'POST':
        giver_info = GiverForm(request.POST)
        if giver_info.isValid():
            giver = giver_info.save(commit=false)
            giver.save()
            return redirect("giver_home")
    else:
        giver_info = GiverForm()
    data = {'giver_info': giver_info}
    return render(request, 'giver_home.html', data)