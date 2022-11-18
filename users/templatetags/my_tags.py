from django import template
from users.models import UserModel
register = template.Library()
from games.models import GameModel

@register.filter()
def is_bought(request, pk):
    games = GameModel.objects.get(id=pk)
    if request.user.games.all().count > 0:
        for game in request.user.games.all:
            if games == game:
                return game


@register.filter()
def is_cart(product, request):
    return product.id in request.session.get('cart', [])

@register.simple_tag()
def cart_info(request):
    return GameModel.get_cart_info(request)

@register.simple_tag()
def get_name(request):
    return GameModel.get_game(request)
#
# @register.filter()
# def bought(request, pk):
