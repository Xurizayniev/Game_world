from django.contrib import admin
from .models import BlogModel, CategoryModel, BlogTagModel

@admin.register(BlogTagModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'tag', 'created_at']
    list_display_links = ['title']
    search_fields = ['title']


@admin.register(CategoryModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']

@admin.register(BlogTagModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['name',]
    list_display_links = ['name']

