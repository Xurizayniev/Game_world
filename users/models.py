from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as tr
from django.db import IntegrityError



class CardModel(models.Model):
    number = models.CharField(max_length=16)
    balance = models.IntegerField(default=5000)


    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

class UserModel(AbstractUser):
    games = models.ManyToManyField('games.GameModel', blank=True, null=True, related_name='games')
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True, verbose_name=tr('avatar'), default='images/users/user_icon.png')
    card = models.OneToOneField(CardModel, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class WishlistModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='wishlists', verbose_name=tr('user'))
    games = models.ForeignKey('games.GameModel', on_delete=models.CASCADE, verbose_name=tr('game'))

    @staticmethod
    def create_or_delete(user, game):
        try:
            return WishlistModel.objects.create(user=user, game=game)
        except IntegrityError:
            return WishlistModel.objects.get(user=user, game=game).delete()

    def __str__(self):
        return f"{self.user.get_full_name()} | {self.games.title}"

    class Meta:
        verbose_name = 'wishlist'
        verbose_name_plural = 'wishlists'
        unique_together = 'user', 'games',

class CommentModel(models.Model):
    post = models.ForeignKey('blog.BlogModel', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'