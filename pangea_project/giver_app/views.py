from django.shortcuts import render
from django.shortcuts import render, redirect

# Create your views here.


def giver_home(request):
    return render(request, 'giver_home.html')