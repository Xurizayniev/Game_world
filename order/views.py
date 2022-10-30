from django.shortcuts import render, redirect
from django.views.generic import *
from .models import OrderHistoryModel
from games.models import GameModel
from .forms import OrderForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from games.models import GameCategoryModel
from blog.models import CategoryModel

@login_required()
def checkoutview(request):
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
            if card.number == form.cleaned_data['card_number'] and card.balance < total_price:
                 card.balance -= total_price
                 user.games.set(game)
                 del request.session['cart']
                 return redirect('games:home')
            else:
                form.add_error('card_number', 'Error')
    return render(request, 'checkout.html', context={
        'username': username,
        'categories': category,
        'blog_categories': blog_categories,
        'form': form
    })

def profile(request):
    user = request.user
    print(user)
    return render(request, 'profile.html', context={
        'user': user
    })
