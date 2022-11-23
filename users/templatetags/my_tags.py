from django import template
register = template.Library()
from games.models import GameModel
from users.models import UserModel


@register.filter()
def is_cart(games, request):
    return games.id in request.session.get('cart', [])

@register.simple_tag()




@register.simple_tag()
def cart_info(request):
    return GameModel.get_cart_info(request)

@register.simple_tag()
def get_name(request):
    return GameModel.get_game(request)

@register.filter()
def bought(user, game):
    return user.games.filter(id=game.id).count() > 0
