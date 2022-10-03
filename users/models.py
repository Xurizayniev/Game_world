from django.db import models
from django.contrib.auth.models import AbstractUser
from games.models import GameModel
from blog.models import BlogModel

class UserModel(AbstractUser):
    games = models.ManyToManyField(GameModel, related_name='games')
    phone = models.CharField(max_length=13)
    balance = models.DecimalField(max_digits=5, decimal_places=2)

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
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, related_name='user')
    post = models.ManyToManyField(BlogModel, related_name='post')
    body = models.TextField()
    like = models.PositiveIntegerField()
    disslike = models.PositiveIntegerField()

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Commemts'