from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    path('blog/', views.blogpage, name='indexblog'),
    url('blog/posts/(?P<id>[0-9]+)$', views.blogshow, name='showblog'),
]
