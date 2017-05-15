from django.conf.urls import url
from .views import blog, blog_post

urlpatterns = [
    url(r'^$', blog, name='blog'),
    url(r'^(?P<post_slug>[-a-zA-Z0-9]+)/?$', blog_post),
]
