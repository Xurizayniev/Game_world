from django import forms
from .models import BlogModel

class CreateBlogForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        exclude = ['created_at', 'user']

