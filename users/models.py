from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as tr


class CardModel(models.Model):
    number = models.CharField(max_length=16)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'


class UserModel(AbstractUser):
    games = models.ManyToManyField('games.GameModel', blank=True, null=True, related_name='games')
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True, verbose_name=tr('avatar'),
                                default='images/users/user_icon.png')
    card = models.OneToOneField(CardModel, on_delete=models.CASCADE, null=True, blank=True)

    @staticmethod
    def get_all_game():
        return UserModel.games.all()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class CommentModel(models.Model):
    post = models.ForeignKey('blog.BlogModel', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user')
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
