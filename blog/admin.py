from django.contrib import admin
from .models import BlogModel, CategoryModel, BlogTagModel
from modeltranslation.admin import TranslationAdmin
@admin.register(BlogModel)
class BlogModelAdmin(TranslationAdmin):
    list_display = ['title', 'category', 'created_at']
    list_display_links = ['title']
    search_fields = ['title']


@admin.register(CategoryModel)
class CategoryModelAdmin(TranslationAdmin):
    list_display = ['name']
    list_display_links = ['name']

@admin.register(BlogTagModel)
class BlogModelAdmin(TranslationAdmin):
    list_display = ['name']
    list_display_links = ['name']
