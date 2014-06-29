from django.shortcuts import render

# Create your views here.

import requests
from django.shortcuts import render, redirect

def charity_home(request):
    return render(request, 'charity_home.html')