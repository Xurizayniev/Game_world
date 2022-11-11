import django.utils.functional
from django.shortcuts import render, redirect
from .models import GameCategoryModel, GameModel, PlatformModel
from blog.models import BlogModel,  CategoryModel
from django.views.generic import TemplateView, ListView

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super(HomePageView, self).get_context_data(**kwargs)
        #Карусель цена
        data['games'] = GameModel.objects.order_by('-price')[:6]
        #new
        data['game'] = GameModel.objects.order_by('-pk')[:10]
        data['video'] = BlogModel.objects.order_by('-pk')[:4]
        data['categories'] = GameCategoryModel.objects.all()
        data['platforms'] = PlatformModel.objects.all()
        data['blog_categories'] = CategoryModel.objects.all()
        data['user'] = self.request.user
        return data

class GameListView(ListView):
    model = GameModel
    template_name = 'games.html'
    context_object_name = 'games'
    paginate_by = 2

    def get_queryset(self):
        qs = GameModel.objects.all().order_by('-id')
        search = self.request.GET.get('game_search')
        if search:
            qs = qs.filter(title__icontains=search)
        cat = self.request.GET.get('category')
        if cat:
            qs = qs.filter(category__name=cat)
        platform = self.request.GET.get('platform')
        if platform:
            qs = qs.filter(platform__name=platform)
        return qs

    def get_context_data(self, **kwargs):
        data = super(GameListView, self).get_context_data(**kwargs)
        data['categories'] = GameCategoryModel.objects.all()
        data['platforms'] = PlatformModel.objects.all()
        data['blog_categories'] = CategoryModel.objects.all()
        data['user'] = self.request.user
        return data


def GameDetail(request, pk):

    object = GameModel.objects.get(pk=pk)
    game = GameModel.objects.order_by('-pk')[:6]
    blogs = BlogModel.objects.order_by('-pk')[:4]
    category = GameCategoryModel.objects.all()
    blog_categories = CategoryModel.objects.all()
    user = request.user
    if request.user.is_authenticated:
        games = user.games.all()
        return render(request, 'game-detail.html', context={
            'object': object,
            'games': game,
            'blogs': blogs,
            'categories': category,
            'blog_categories': blog_categories,
            'user': user,
            'buy': games
    })
    else:
        return render(request, 'game-detail.html', context={
            'object': object,
            'games': game,
            'blogs': blogs,
            'categories': category,
            'blog_categories': blog_categories,
            'user': user,
        })

class VideoListView(ListView):
    model = GameModel
    template_name = "video.html"
    context_object_name = 'games'
    paginate_by = 2

    def get_queryset(self):
        qs = GameModel.objects.all().order_by('-id')
        search = self.request.GET.get('game_search')
        if search:
            qs = qs.filter(title__icontains=search)
        cat = self.request.GET.get('category')
        if cat:
            qs = qs.filter(category__name=cat)
        platform = self.request.GET.get('platform')
        if platform:
            qs = qs.filter(platform__name=platform)
        return qs

    def get_context_data(self, **kwargs):
        data = super(VideoListView, self).get_context_data(**kwargs)
        data['categories'] = GameCategoryModel.objects.all()
        data['platforms'] = PlatformModel.objects.all()
        data['blog_categories'] = CategoryModel.objects.all()
        data['user'] = self.request.user
        return data

def update_cart_view(request, id):
    cart = request.session.get('cart', [])

    if id in cart:
        cart.remove(id)
    else:
        cart.append(id)

    request.session['cart'] = cart
    return redirect(request.GET.get('next', '/'))
