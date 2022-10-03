from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import UserModel, CommentModel
from django.utils.translation import gettext_lazy as tr

class CategoryModel(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class BlogTagModel(models.Model):
    name = models.CharField(max_length=60, verbose_name=tr('name'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created_at'))
        
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

class WithVisitCounter(models.Model):
    visits = models.IntegerField(editable=False, default=0)

    class Meta:
        abstract = True


class BlogModel(WithVisitCounter, models.Model):
    title = models.CharField(max_length=150, verbose_name=tr('title'))
    body = RichTextUploadingField()
    image = models.ImageField(upload_to='blog/', verbose_name=tr('image'))
    image_body = models.ImageField(upload_to='blog/', verbose_name=tr('image body'))
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, verbose_name=tr('user'))
    comment = models.ForeignKey(CommentModel, on_delete=models.SET_NULL, verbose_name=tr('comment'))
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, verbose_name=tr('category'))
    tags = models.ManyToManyField(BlogTagModel, verbose_name=tr('tags'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=tr('created_at'))
        
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'