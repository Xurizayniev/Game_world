from modeltranslation.translator import translator, TranslationOptions
from .models import *


class CategoryModelTranslation(TranslationOptions):
    fields = ('name',)

class GameModelTranslation(TranslationOptions):
    fields = ('title', 'body')

translator.register(GameModel, GameModelTranslation)
translator.register(GameCategoryModel, CategoryModelTranslation)