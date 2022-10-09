from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogModel
from .forms import CreateBlogForm
from users.models import CommentModel, UserModel
from django.contrib.auth.decorators import login_required
from users.forms import CommentForm

class BlogListView(ListView):
    template_name = 'blog-list.html'


    def get_queryset(self):
        qs = BlogModel.objects.order_by('-id')
        author = self.request.GET.get('author')
        if author:
            qs = qs.filter(author__username=author)
            print('Author')
        return qs
        

class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'blog-detail.html'


def create_post(request):
    form = CreateBlogForm
    
    if request.method == 'POST':
        form = CreateBlogForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print('rfuurfuhffhjd')
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog:news')
        
    return render(request, 'blog-create.html', context={
        'form': form
    })



def blogdetail(request, pk):
    """Вывод полной статьи
    """
    post = get_object_or_404(BlogModel, id=pk)
    comment = CommentModel.objects.filter(post=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            print('POST')
            form = form.save(commit=False)
            form.author = request.user
            form.post = post
            form.save()
            return redirect('blog-detail.html', pk)
    else:
        form = CommentForm()
    return render(request, "blog-detail.html",
                  {"post": post,
                   "comment": comment,
                   "form": form})