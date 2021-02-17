from django.shortcuts import render, redirect
from login.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.forms import inlineformset_factory

from .models import *
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
import urllib, json
from django.conf import settings


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                user = form.save()
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return redirect('login:register')

            # user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customers')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('login:login')

    context = {'form': form}
    return render(request, 'login/register.html', context)


@unauthenticated_user
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req = urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            if result['success']:
                login(request, user)
                return redirect('login:home')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return redirect('login:login')

        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login/login.html', context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('login:login')


@login_required(login_url='login:login')
def home(request):
    return render(request, 'login/dashboard.html')


def userPage(request):
    context = {}
    return render(request, 'login/user.html', context)
