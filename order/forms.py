from django import forms
from .models import OrderHistoryModel
from django.utils.translation import gettext_lazy as tr

class OrderForm(forms.Form):
    card_number = forms.CharField(widget=forms.PasswordInput(), label=tr('card_number'))