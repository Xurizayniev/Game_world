from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import *
from .forms import *
from django.contrib.auth import login, authenticate
from django.core.exceptions import ValidationError
from .models import *
from games.models import GameCategoryModel, GameModel
from blog.models import CategoryModel
from django.http import HttpResponse
import random

def loginview(request):
    form = LoginForm()
    categories = GameCategoryModel.objects.all()
    blog_categories = CategoryModel.objects.all()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('games:home')
            else:
                form.add_error('password', 'Login or password incorrect')
                
    return render(request, 'login.html', context={
        'form': form,
        'categories': categories,
        'blog_categories': blog_categories,

    })



def user_registration(request):
    form = RegistrationForm()
    categories = GameCategoryModel.objects.all()
    blog_category = CategoryModel.objects.all()

    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            del form.cleaned_data['confirm_password']
            num = random.randrange(1000000000000000, 9999999999999999)
            user = form.save(commit=False)
            user.set_password(user.password)
            user.card = CardModel.objects.create(number=num)
            request.session.get('cart', [])
            user.save()
            return redirect('users:login')
    return render(request, 'register.html', context={
        'form': form,
        'categories': categories,
        'blog_categories': blog_category
    })
