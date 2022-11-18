from django.db import models
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import UserModel

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
    average_rating = models.FloatField(verbose_name=_('Average rating'), default=0.0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))


    @staticmethod
    def get_cart_info(request):
        cart = request.session.get('cart', [])
        if not cart:
            return 0, 0.0
        return len(cart), GameModel.objects.filter(id__in=cart).aggregate(Sum('price'))['price__sum']

    @staticmethod
    def get_game(request):
        cart = request.session.get('cart', [])
        if not cart:
            return None
        return GameModel.objects.filter(id__in=cart)


    @staticmethod
    def get_cart_objects(request):
        cart = request.session.get('cart', [])
        if not cart:
            return None
        return GameModel.objects.filter(id__in=cart)


class RatingModel(models.Model):
    user = models.ForeignKey('users.UserModel', on_delete=models.CASCADE, null=True, blank=True)
    game = models.ForeignKey(GameModel, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField(max_length=500, null=True, blank=True)
    rating = models.FloatField()
    like = models.ManyToManyField('users.UserModel', related_name=_('like'), null=True, blank=True,)
    dislike = models.ManyToManyField('users.UserModel', related_name=_('dislike'), null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

