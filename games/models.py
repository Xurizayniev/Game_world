from re import M
from django.db import models
from django.utils.translation import gettext_lazy as tr
from ckeditor_uploader.fields import RichTextUploadingField


class GameCategoryModel(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Game_category'
        verbose_name_plural = 'Game_categories'


class CompanyModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=tr('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created_at'))
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class PlatformModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=tr('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created_at'))
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Platform'
        verbose_name_plural = 'Platforms'



class GameModel(models.Model):
    title = models.CharField(max_length=150, verbose_name=tr('title'))
    body = RichTextUploadingField()
    image = models.ImageField(upload_to='games/', verbose_name=tr('image'))
    image_body = models.ImageField(upload_to='games/', verbose_name=tr('image body'))
    image_body2 = models.ImageField(upload_to='games/', verbose_name=tr('image body'))
    image_body3 = models.ImageField(upload_to='games/', verbose_name=tr('image body'))
    video = models.FileField()
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, verbose_name=tr('company'))
    comment = models.ForeignKey('users.CommentModel', on_delete=models.SET_NULL, verbose_name=tr('comment'), null=True, blank=True)
    category = models.ForeignKey(GameCategoryModel, on_delete=models.SET_NULL, verbose_name=tr('category'), null=True)
    platform = models.ManyToManyField(PlatformModel, verbose_name=tr('platform'))
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # grade =...
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'