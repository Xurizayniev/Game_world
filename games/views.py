from statistics import quantiles
from unicodedata import category
from django.shortcuts import render
from .models import GameCategoryModel, GameModel, PlatformModel
from blog.models import BlogModel, BlogTagModel
from django.views.generic import TemplateView, DetailView, ListView

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

class VideoListView(ListView):
    model = GameModel
    template_name = "video.html"
    context_object_name = 'games'

    def get_queryset(self):
        qs = GameModel.objects.all().order_by('-id')

        search = self.request.GET.get('game_search')
        if search:
            qs = qs.filter(title__icontains=search)
        cat = self.request.GET.get('category')
        if cat:
            qs = qs.filter(category_id=cat)
        return qs

    def get_context_data(self, **kwargs):
        data = super(VideoListView, self).get_context_data(**kwargs)
        data['categories'] = GameCategoryModel.objects.all()
        data['platforms'] = PlatformModel.objects.all()
        return data