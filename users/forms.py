from pyexpat import model
from unicodedata import name
from django import forms
from .models import CommentModel, UserModel
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as tr


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), label=tr('username'))
    password = forms.CharField(widget=forms.PasswordInput(), label=tr('password'))



class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=(
        forms.PasswordInput(attrs={'class': 'form-control'})

    ), required=True)

    def clean_confirm_password(self, *args, **kwargs):

        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Passwords are not the same !')
        return self.cleaned_data

    class Meta:
        model = UserModel
        fields = ['username', 'password', 'confirm_password']


class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['email', 'body']