from django.shortcuts import render, redirect, reverse
from games.models import GameModel, GameCategoryModel
from .forms import OrderForm
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from blog.models import CategoryModel
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
            else:
                form.add_error('price', 'Error')
    return render(request, 'checkout.html', context={
        'username': username,
        'categories': category,
        'blog_categories': blog_categories,
        'form': form
    })

def profile(request):
    user = request.user
    games = user.games.all()
    print(type(games))
    return render(request, 'profile.html', context={
        'user': user,
        'games': games,
    })
