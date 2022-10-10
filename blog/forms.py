from tkinter import Widget
from django import forms
from .models import BlogModel, UserModel, CategoryModel, BlogTagModel

class CreateBlogForm(forms.form):
        title = forms.CharField(max_length=150)
        body = forms.Textarea()
        image = forms.ImageField()
        image_body = forms.ImageField(upload_to='blog/', verbose_name=tr('image body'))
        author = forms.ForeignKey(UserModel)
        category = forms.ForeignKey(CategoryModel)
        tags = forms.ManyToManyField(BlogTagModel)
