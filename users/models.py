from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as tr


class UserModel(AbstractUser):
    games = models.ManyToManyField('games.GameModel', blank=True, null=True, related_name='games')
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True, verbose_name=tr('avatar'))

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class CardModel(models.Model):
    number = models.CharField(max_length=16)
    balance = models.IntegerField(default=5000)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'
        
class WithVisitCounter(models.Model):
    visits = models.IntegerField(editable=False, default=0)

    class Meta:
        abstract = True


class CommentModel(WithVisitCounter, models.Model):
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