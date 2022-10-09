from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import BlogModel
from .forms import CreateBlogForm
from users.models import UserModel
from django.contrib.auth.decorators import login_required


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


@login_required
def create_post(request):
    context = {}
    form = CreateBlogForm(request.POST, files=request.FILES)
    if request.method == "POST":
        
        if form.is_valid():
            print("\n\n jhiunkjn")
            author = UserModel.objects.get(user=request.user)
            data = form.save(commit=False)
            data.user = author
            data.save()

            return redirect('blog:news')
        
    context.update({
            'form': form,
            'title': 'Create New Post'
    })
    return render(request, 'blog-create.html', context)
