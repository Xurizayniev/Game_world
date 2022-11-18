from django import forms

from .models import RatingModel

class RatingForm(forms.ModelForm):

    class Meta:
        model = RatingModel
        fields = ('rating', 'subject', 'comment')