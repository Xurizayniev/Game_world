from modeltranslation.translator import translator, register, TranslationOptions
from .models import *

@register(BlogModel)
class BlogModelTranslation(TranslationOptions):
    fields = ('title', 'body')


@register(CategoryModel)
class CategoryModelTranslation(TranslationOptions):
    fields = ('name',)

@register(BlogTagModel)
class PlatformModelTranslation(TranslationOptions):
    fields = ('name',)
