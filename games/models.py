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

DEFAULT_CHOICES = {
    '5': 'Отлично',
    '4': 'Хорошо',
    '3': 'Нормально',
    '2': 'Плохо',
    '1': 'Ужасно',
}



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
    # average_rating = models.FloatField(verbose_name=_('Average rating'), default=0,)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def get_platform(self):
        return self.platform


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


#     def get_averages(self, max_value=None):
#         max_rating_value = 0
#         game_maximums = {}
#         game_averages = {}
#         games = GameModel.objects.filter(counts_for_average=True, value__comment=self)
#         # Высчитываем среднее значение каждого поста
#         for game in games:
#             game_average = None
#             ratings = ReviewModel.objects.filter(comment=self, game=game, value__isnull=False).exclude(value='')
#             game_max = game_maximums[game]
#             for comment in ReviewModel:
#                 if game_average is None:
#                     game_average = float(comment.value)
#                 else:
#                     game_average += float(comment.value)
#
#             if game_average is not None:
#                 game_average *= float(max_rating_value) / float(game_max)
#                 game_averages[game] = (game_average / ratings.count())
#
#         total_average = 0
#         for game, game_average in game_averages.posts():
#             total_average += game_average
#         if not len(game_averages):
#             return (False, False)
#         total_average /= len(game_averages)
#
#         return total_average, game_averages
#
#     def get_average_rating(self, max_value=None):
#         total_average, game_averages = self.get_averages(max_value=max_value)
#         return total_average
#
#     def get_post_averages(self, max_value=None):
#         total_average, game_averages = self.get_averages(max_value=max_value)
#         return game_averages
#
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Game'
#         verbose_name_plural = 'Games'
#
# class ReviewModel(models.Model):
#     rating_choices = models.IntegerField(choices=DEFAULT_CHOICES)
#     value = models.CharField(
#         max_length=20,
#         verbose_name=_('Value'),
#         choices=rating_choices,
#         blank=True, null=True
#     )
#     games = models.ForeignKey(GameModel, on_delete=models.CASCADE, related_name='review')  # делаем отношение "один ко многим", что бы в статье можно было оставлять несколько комментариев
#     author = models.ForeignKey('users.UserModel', on_delete=models.CASCADE, related_name='us')
#     name = models.CharField(max_length=80)
#     title = models.CharField(max_length=50)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
