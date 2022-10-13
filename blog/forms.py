from django import forms
from django.forms import Textarea, Widget
from .models import BlogModel, UserModel, CategoryModel, BlogTagModel

# class CreateBlogForm(forms.Form):
        # title = forms.CharField(max_length=150)
        # body = forms.CharField(widget=forms.Textarea)
        # image = forms.ImageField()
        # image_body = forms.ImageField()
        # category = forms.ModelChoiceField(queryset=CategoryModel.objects.all())
        # tags = forms.ModelChoiceField(queryset=BlogTagModel.objects.all())

class CreateBlogForm(forms.ModelForm):

        class Meta:
                model = BlogModel
                fields = ['title', 'body', 'image', 'image_body', 'category', 'tags']

        tags = forms.ModelMultipleChoiceField(queryset=BlogTagModel.objects.all(), widget=forms.CheckboxSelectMultiple)