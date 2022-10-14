from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class GameCategoryModel(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Game_category'
        verbose_name_plural = 'Game_categories'


class CompanyModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class PlatformModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Platform'
        verbose_name_plural = 'Platforms'



class GameModel(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    body = RichTextUploadingField()
    poster = models.ImageField(upload_to='games/poster/', verbose_name=_('poster'))
    image_body = models.ImageField(upload_to='games/', verbose_name=_('image body'))
    image_body2 = models.ImageField(upload_to='games/', verbose_name=_('image body'))
    image_body3 = models.ImageField(upload_to='games/', verbose_name=_('image body'))
    image_body4 = models.ImageField(upload_to='games/', verbose_name=_('image body'))
    video = models.URLField()
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, verbose_name=_('company'))
    category = models.ForeignKey(GameCategoryModel, on_delete=models.SET_NULL, verbose_name=_('category'), null=True)
    platform = models.ManyToManyField(PlatformModel, verbose_name=_('platform'))
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def get_platform(self):
        return self.platform

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

class RatingStarModel(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{int(self.value)}'

    class Meta:
        verbose_name = "Star rating"
        verbose_name_plural = "Stars rating"
        ordering = ["-value"]


class RatingModel(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    title = models.CharField(max_length=50)
    review = models.TextField()
    star = models.ForeignKey(RatingStarModel, on_delete=models.CASCADE, verbose_name="star")
    game = models.ForeignKey(GameModel, on_delete=models.CASCADE, verbose_name="game")
    user = models.ForeignKey('users.UserModel', on_delete=models.CASCADE, verbose_name='user')
    like = models.PositiveIntegerField(default=0, verbose_name=_('likes'))
    disslike = models.PositiveIntegerField(default=0, verbose_name=_('disslike'))

    def __str__(self):
        return f"{self.star} - {self.game}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

