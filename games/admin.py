from django.contrib import admin
from .models import GameModel, PlatformModel, GameCategoryModel, CompanyModel, RatingModel
from modeltranslation.admin import TranslationAdmin

@admin.register(PlatformModel)
class PlatformModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_display_links = ['name']
    search_fields = ['name']

@admin.register(RatingModel)
class RatingModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject']
    list_display_links = ['subject',]
    search_fields = ['user']


class GameCategoryModelAdmin(TranslationAdmin):
    list_display = ['name', 'created_at']
    list_display_links = ['name']
    search_fields = ['name']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(CompanyModel)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_display_links = ['name']
    search_fields = ['name']

class GameModelAdmin(TranslationAdmin):
    list_display = ['title', 'category', 'created_at', ]
    list_display_links = ['title']
    search_fields = ['title']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(GameModel, GameModelAdmin)
admin.site.register(GameCategoryModel, GameCategoryModelAdmin)