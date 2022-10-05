from django.contrib import admin
from .models import UserModel, CardModel

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
