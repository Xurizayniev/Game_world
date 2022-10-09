from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from .models import * 
from django.http import HttpResponse

def loginview(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('blog:news')
                
    return render(request, 'login.html', context={
        'form': form
    })


def user_registration(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            return redirect('users:login')
    
    return render(request, 'register.html', context={
        'form': form
    })
    