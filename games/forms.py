from django import forms

from .models import RatingStarModel, RatingModel


class RatingForm(forms.ModelForm):
    """Форма добавления рейтинга"""
    star = forms.ModelChoiceField(
        queryset=RatingStarModel.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = RatingModel
        fields = ("star",)