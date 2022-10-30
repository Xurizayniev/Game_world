from django.db import models
from users.models import UserModel
from games.models import GameModel
# Create your models here.

class OrderHistoryModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True, blank=True)
    games = models.ManyToManyField(GameModel)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.games.name}"

    class Meta:
        verbose_name = 'History'
