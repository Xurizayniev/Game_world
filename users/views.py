from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Sum
from .forms import *
from django.contrib.auth import login, authenticate
from .models import *
from games.models import GameCategoryModel, GameModel
from blog.models import CategoryModel
from django.contrib import messages
from django.utils.translation import gettext_lazy as tr
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
            messages.success(request, tr('Registration is successfully done'))
            return redirect('users:login')
    return render(request, 'register.html', context={
        'form': form,
        'categories': categories,
        'blog_categories': blog_category
    })

@login_required()
def checkoutview(request):
    session = request.session.get('cart', [])
    if len(session) == 0:
        return redirect(reverse('games:home'))
    form = OrderForm
    user = request.user
    game = GameModel.get_cart_objects(request)
    total_price = game.aggregate(Sum('price')).get('price__sum', '')
    username = request.user.username
    card = request.user.card
    category = GameCategoryModel.objects.all()
    blog_categories = CategoryModel.objects.all()
    if request.method == 'POST':
        form = OrderForm(data=request.POST)
        if form.is_valid():
            if total_price == form.cleaned_data['price']:
                 card.balance -= total_price
                 user.games.add(*game)
                 card.balance -= total_price
                 card.save()
                 request.session['cart'] = []
                 return redirect('games:home')
            elif total_price > form.cleaned_data['price']:
                form.add_error('price', tr("insufficient funds"))
            else:
                form.add_error('price', tr('the amount was entered incorrectly'))
    return render(request, 'checkout.html', context={
        'username': username,
        'categories': category,
        'blog_categories': blog_categories,
        'form': form
    })

def profileview(request):
    user = request.user
    games = user.games.all()
    paginator = Paginator(games, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'profile.html', context={
        'user': user,
        'page_obj': page_obj,
    })





