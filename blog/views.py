from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from games.models import GameModel
from .models import BlogModel
from .forms import CreateBlogForm
from users.models import CommentModel, UserModel
from django.contrib.auth.decorators import login_required
from users.forms import CommentForm

class BlogListView(ListView):
    template_name = 'blog-list.html'
    paginate_by = 1


    def get_queryset(self):
        qs = BlogModel.objects.order_by('-id')
        tag = self.request.GET.get('tags')
        if tag:
            qs = qs.filter(tags=tag)
            print('tag', tag)
        cat = self.request.GET.get('category')
        if cat:
            qs = qs.filter(category=cat)
        author = self.request.GET.get('author')
        if author:
            qs = qs.filter(author__username=author)
            print('Author')
        return qs

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['games'] = GameModel.objects.order_by('-pk')[:2]
        data['blogs'] = BlogModel.objects.order_by('pk')[:4]
        return data
        
class BlogCreateView(CreateView):
    template_name = 'blog-create.html'
    form_class = CreateBlogForm

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        form.save_m2m()
        return redirect('blog:news')


# def create_post(request):
#     form = CreateBlogForm()
#     if request.method == 'POST':
#         form = CreateBlogForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)
#             blog = BlogModel.objects.create(
#                 title = form.cleaned_data.get('title'),
#                 body = form.cleaned_data.get('body'),
#                 image = form.cleaned_data.get('image'),
#                 image_body = form.cleaned_data.get('image_body'),
#                 author = request.user,
#                 category = form.cleaned_data['category'],
#                 tags = form.cleaned_data['tags']
#             )
#             print(f"{blog.title} {blog.author} {blog.tags} {blog.category}")
#             blog.save()
#             try:
#                 BlogModel.objects.create(**form.cleaned_data)
#             except:
#                 form.add_error(None, 'error')

#             return redirect('blog:news')
        
#     return render(request, 'blog-create.html', context={
#         'form': form
#     })



def blogdetail(request, pk):
    post = get_object_or_404(BlogModel, id=pk)
    games = GameModel.objects.order_by('-pk')[:2]
    blogs = BlogModel.objects.order_by('-pk')[:4]
    comment = CommentModel.objects.filter(post=pk)
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
                   "comment": comment,
                   "form": form,
                   'games': games,
                   'blogs': blogs
                })




