from django import forms
from django.utils.translation import gettext_lazy as tr

class OrderForm(forms.Form):
    price = forms.IntegerField(label=tr('price'))