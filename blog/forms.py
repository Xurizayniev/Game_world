from django import forms
from .models import BlogModel

class CreateBlogForm(forms.ModelForm):

    class Meta:
        model = BlogModel
        fields = ['title', 'body', 'image', 'image_body', 'category', 'tags']
        widget = {
            'body': forms.Textarea(
                attrs={
                    'placeholder': "body"
                }
            )
        }


