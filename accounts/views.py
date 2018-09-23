from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm



def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return render(request, 'after-login.html')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})