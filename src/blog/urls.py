from django.urls import path

from .views import index, article

urlpatterns = [
    path('', index, name='blog-index'),
    path('article-<int:num_article>/<str:title>/', article, name='article-dynamic')
]
