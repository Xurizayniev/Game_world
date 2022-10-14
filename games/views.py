from django.shortcuts import render
from .models import GameModel
from blog.models import BlogModel, BlogTagModel
from django.views.generic import TemplateView, DetailView

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super(HomePageView, self).get_context_data(**kwargs)
        #Карусель цена
        data['games'] = GameModel.objects.order_by('-price')[:6]
        #new
        data['game'] = GameModel.objects.order_by('-pk')[:10]
        data['video'] = BlogModel.objects.order_by('-pk')[:4]
        return data

def GameDetail(request, pk):
    object = GameModel.objects.get(pk=pk)
    game = GameModel.objects.order_by('-pk')[:6]
    blogs = BlogModel.objects.order_by('-pk')[:4]
    return render(request, 'game-detail.html', context={
        'object': object,
        'games': game,
        'blogs': blogs,

    })

