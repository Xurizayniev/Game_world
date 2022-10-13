from django.contrib import admin
from .models import GameModel, PlatformModel, GameCategoryModel, CompanyModel, RatingStarModel, RatingModel

@admin.register(GameModel)
class GameModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_display_links = ['title']
    search_fields = ['title']


@admin.register(PlatformModel)
class PlatformModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_display_links = ['name']
    search_fields = ['name']
    

@admin.register(GameCategoryModel)
class GameCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_display_links = ['name']
    search_fields = ['name']
    

@admin.register(CompanyModel)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_display_links = ['name']
    search_fields = ['name']

@admin.register(RatingModel)
class RatingModelAdmin(admin.ModelAdmin):
    list_display = ['game', 'review', 'title']
    list_display_links = ['game', 'review']

@admin.register(RatingStarModel)
class RatingStarModelAdmin(admin.ModelAdmin):
    list_display = ['value']
    list_display_links = ['value']

    








class Media:
    js = (
        'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
        'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
        'modeltranslation/js/tabbed_translation_fields.js',
    )
    css = {
        'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
    }
