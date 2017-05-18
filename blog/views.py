from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from .models import Post

def blog(request):
    posts = Post.objects.order_by('-date')
    pages = Paginator(posts, 5)

    page = request.GET.get('page')
    if not page:
        page = 1

    try:
        returned_page = pages.page(page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)
    return render_to_response('blog/blog.html', { 'posts': returned_page})


def blog_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return render_to_response('blog/post.html', { 'post': post})
