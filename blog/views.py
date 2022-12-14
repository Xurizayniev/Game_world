from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from games.models import GameModel, GameCategoryModel
from .models import BlogModel, CategoryModel
from .forms import CreateBlogForm
from users.models import CommentModel, UserModel
from django.contrib.auth.decorators import login_required
from users.forms import CommentForm
from django.core.paginator import Paginator

class BlogListView(ListView):
    template_name = 'blog-list.html'
    paginate_by = 1


    def get_queryset(self):
        qs = BlogModel.objects.order_by('-id')
        tag = self.request.GET.get('tags')
        if tag:
            qs = qs.filter(tags__name=tag)
        cat = self.request.GET.get('category')
        if cat:
            qs = qs.filter(category__name=cat)
        author = self.request.GET.get('author')
        if author:
            qs = qs.filter(author__username=author)
        return qs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['games'] = GameModel.objects.order_by('-pk')[:2]
        data['blogs'] = BlogModel.objects.order_by('pk')[:4]
        data['categories'] = GameCategoryModel.objects.all()
        data['blog_categories'] = CategoryModel.objects.all()
        data['user'] = self.request.user
        return data
        
class BlogCreateView(CreateView):
    template_name = 'blog-create.html'
    form_class = CreateBlogForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        form.save_m2m()
        self.request.user.card.balance += 10
        self.request.user.card.save()
        return redirect('blog:news')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = GameCategoryModel.objects.all()
        data['blog_categories'] = CategoryModel.objects.all()
        data['user'] = self.request.user
        data['card_balance'] = self.request.user.card.balance
        return data


def blogdetail(request, pk):
    post = get_object_or_404(BlogModel, id=pk)
    games = GameModel.objects.order_by('-pk')[:2]
    blogs = BlogModel.objects.order_by('-pk')[:4]
    category = GameCategoryModel.objects.all()
    blog_categories = CategoryModel.objects.all()
    popular = GameModel.objects.order_by('average_rating')
    comment = CommentModel.objects.filter(post=pk).order_by('-id')
    paginator = Paginator(comment, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    user = request.user
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            print('POST')
            com = form.save(commit=False)
            com.author = request.user
            com.post = post
            com.save()
            return redirect('blog:detail', pk)
    else:
        form = CommentForm()
    return render(request, "blog-detail.html",
                {  "post": post,
                   "page_obj": page_obj,
                   "form": form,
                   'games': games,
                   'blogs': blogs,
                   'categories': category,
                   'blog_categories': blog_categories,
                   'popular': popular,
                   'user': user,
                })