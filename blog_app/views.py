from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = "blog/post/list.html"


def get_objet_or_404():
    pass


def post_detail(request, year, month, day, slug):
    post = get_objet_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month,publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
