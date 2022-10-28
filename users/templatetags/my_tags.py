from django import template

register = template.Library()
from users.models import WishlistModel
from games.models import GameModel

@register.filter()
def is_wishlist(game, request):
    return WishlistModel.objects.filter(user=request.user, game=game).exists()

@register.filter()
def is_cart(product, request):
    return product.id in request.session.get('cart', [])

@register.simple_tag()
def cart_info(request):
    return GameModel.get_cart_info(request)

@register.simple_tag()
def get_name(request):
    return GameModel.get_game(request)




