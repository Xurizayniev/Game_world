from turtle import home
from django.shortcuts import render
from games.models import GameModel
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super(HomePageView, self).get_context_data(**kwargs)
        data['games'] = GameModel.objects.order_by('-pk')[:5]
        