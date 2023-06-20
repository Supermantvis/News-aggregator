from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.NewsArticleListView.as_view(), name='articles'),
    path('article/<int:pk>', views.NewsArticleDetailView.as_view(), name='article_detail'),
]
