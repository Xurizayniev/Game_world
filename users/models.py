from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    games = models.ManyToManyField('games.GameModel', related_name='games')

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
    post = models.ForeignKey('blog.BlogModel', related_name='comments')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.PositiveIntegerField()
    disslike = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Commemts'