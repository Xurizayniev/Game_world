from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import GameCategoryModel, GameModel, PlatformModel, RatingModel
from blog.models import BlogModel,  CategoryModel
from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super(HomePageView, self).get_context_data(**kwargs)
        #Carousel popular
        data['games'] = GameModel.objects.order_by('average_rating')[:6]
        #new
        data['game'] = GameModel.objects.order_by('-pk')[:10]
        data['video'] = BlogModel.objects.order_by('-pk')[:4]
        data['categories'] = GameCategoryModel.objects.all()
        data['platforms'] = PlatformModel.objects.all()
        data['blog_categories'] = CategoryModel.objects.all()
        data['user'] = self.request.user
        data['rating'] = RatingModel.objects.all().order_by('pk')[:3]
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
        data['popular'] = GameModel.objects.order_by('average_rating')
        return data


def GameDetail(request, pk, **kwargs):
    object = GameModel.objects.get(pk=pk)
    all_ratings = RatingModel.objects.filter(game_id=pk).order_by('-id')
    paginator = Paginator(all_ratings, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    all_rate_count = RatingModel.objects.filter(game_id=pk).count()
    if len(all_ratings) != 0:
        all_rate = sum([all_rate.rating for all_rate in all_ratings])
        all_rate = all_rate/all_rate_count
        # all_rate = all_rate*100/5
        object.average_rating = all_rate
        object.save()
    url = request.META.get('HTTP_REFERER')
    game = GameModel.objects.order_by('-pk')[:6]
    blogs = BlogModel.objects.order_by('-pk')[:4]
    category = GameCategoryModel.objects.all()
    blog_categories = CategoryModel.objects.all()
    popular = GameModel.objects.order_by('average_rating')[:2]
    user = request.user
    if request.method == "POST":
        print(request.POST)
        if request.POST['subject']:
            data, ob = RatingModel.objects.get_or_create(user=user, game_id=pk)
            data.subject = request.POST.get('subject')
            data.comment = request.POST.get('comment')
            data.rating = request.POST.get('rating')
            data.save()
            return redirect(url)

    if request.user.is_authenticated:
        games = user.games.all()
        return render(request, 'game-detail.html', context={
            'object': object,
            'page_obj': page_obj,
            'games': game,
            'blogs': blogs,
            'categories': category,
            'blog_categories': blog_categories,
            'user': user,
            'buy': games,
            'all_ratings': all_ratings,
            'popular': popular,
    })
    else:
        return render(request, 'game-detail.html', context={
            'object': object,
            'page_obj': page_obj,
            'games': game,
            'blogs': blogs,
            'categories': category,
            'blog_categories': blog_categories,
            'user': user,
            'all_ratings': all_ratings,
            'popular': popular,
        })

@login_required
def like_dislike(request, pk):
    rating = RatingModel.objects.get(pk=pk)
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        if request.POST.get('send') == 'like':
            if rating.like.filter(id=request.user.id).count() > 0:
                rating.like.remove(request.user)
            elif rating.dislike.filter(id=request.user.id).count() > 0:
                rating.dislike.remove(request.user)
                rating.like.add(request.user)
            else:
                rating.like.add(request.user)
            rating.save()
        elif request.POST.get('send') == 'dislike':
            if rating.dislike.filter(id=request.user.id).count() > 0:
                rating.dislike.remove(request.user)
            elif rating.like.filter(id=request.user.id).count() > 0:
                rating.like.remove(request.user)
                rating.dislike.add(request.user)
            else:
                rating.dislike.add(request.user)
            rating.save()
    return redirect(url)
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
