from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import generic
from django.contrib.auth import get_user_model


from customauth.forms import SignUpForm, UpdateProfileForm

# Create your views here.

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def loginview(request):
    return redirect('profile')

def logoutview(request):
    return redirect('/')


def subscription(request):
    return render(request, 'account/subscription.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            print("saved user")
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('/account/profile')
    else:
        initial = {
            'email': request.user.email,
        }
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'account/profile.html', {'form': form, 'user': request.user})
