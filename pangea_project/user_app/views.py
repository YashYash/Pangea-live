from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from user_app.forms import SignupForm, LoginForm
from charity_app.models import Video, Charity


def signup(request):
    if request.method == "POST":
        print("request was made")
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data["username"],
                form.cleaned_data["email"],
                form.cleaned_data["password"],
            )
        return redirect("login")

    else:
        form = SignupForm()
    data = {'form': form}
    return render(request, "signup.html", data)



def login1(request):
    if request.method == "POST":
        form1 = LoginForm(request.POST)
        if form1.is_valid():
            user = authenticate(username=form1.cleaned_data['username'], password=form1.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("landing")

    else:
        form1 = LoginForm()
    data = {'form1': form1}
    return render(request, "landing", data)


def landing(request):
    all_videos = Video.objects.all()
    data = {'all_videos' : all_videos}
    return render(request, 'landing.html', data)


def charity_like(request, charity_id):
    charity = Charity.objects.get(id=charity_id)
    data = {"charity": charity}
    return render(request, 'charity_like.html', data)