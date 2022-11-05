from django import template
from users.models import UserModel
register = template.Library()
from games.models import GameModel

# @register.filter()
# def is_wishlist(game, request):
#     return WishlistModel.objects.filter(user=request.user, game=game).exists()

@register.filter()
def is_cart(product, request):
    return product.id in request.session.get('cart', [])

@register.simple_tag()
def cart_info(request):
    return GameModel.get_cart_info(request)

@register.simple_tag()
def get_name(request):
    return GameModel.get_game(request)

@register.simple_tag()
def bought(request, id):
    user_games = request.user.games.all()
    id = GameModel.objects.filter(id)
    if user_games in id:
        return UserModel.get_game()
    return None