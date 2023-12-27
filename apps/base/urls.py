from django.urls import path
from apps.base import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('gallery/', views.gallery, name = 'gallery'),
    path('list_price/', views.list_price, name='list_price'),
    path('news/', views.news, name = 'news'),
    path('contact/', views.contact, name='contact'),
    path('blog_news/<int:id>/', views.blog_news, name='blog_news')
]