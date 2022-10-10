from django.contrib import admin
from .models import UserModel, CardModel, CommentModel

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username']
    list_display_links = ['username']
    search_fields = ['username']


@admin.register(CardModel)
class CardModelAdmin(admin.ModelAdmin):
    list_display = ['number']
    list_display_links = ['number']
    search_fields = ['number']

@admin.register(CommentModel)
class CardModelAdmin(admin.ModelAdmin):
    list_display = ['body']
    list_display_links = ['body']
    search_fields = ['body']
