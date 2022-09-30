from django.contrib import admin
from .models import UserModel, CardModel

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'phone', 'first_name', 'balance']
    list_display_links = ['username']
    search_fields = ['username']


@admin.register(CardModel)
class CardModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']
    list_display_links = ['user']

    