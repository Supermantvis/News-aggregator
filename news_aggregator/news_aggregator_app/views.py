from typing import Any, Dict
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _
from django.views import generic
from django.urls import reverse
from . models import Category, NewsArticle, Comment
from . forms import ArticleCommentForm


def home(request):
    # Suskaičiuokime keletą pagrindinių objektų
    num_articles = NewsArticle.objects.all().count()
    num_categories= Category.objects.all().count()

    # Apsilankymų skaitliukas
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    
    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_articles': num_articles,
        'num_categories': num_categories,
        'num_visits': num_visits,
    }

    return render(request, 'news_aggregator_app/home.html', context)


class NewsArticleListView(generic.ListView):
    model = NewsArticle
    paginate_by = 5
    template_name = 'news_aggregator_app/articles_list.html'
    ordering = ['published_at']

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
                # Q(author__last_name__istartswith=query)
            )
        return qs
    

class NewsArticleDetailView(generic.edit.FormMixin, generic.DetailView):
    model = NewsArticle
    template_name = 'news_aggregator_app/article_detail.html'
    form_class = ArticleCommentForm

    def get_initial(self) -> Dict[str, Any]:
        initial = super().get_initial()
        initial['article'] = self.get_object()
        initial['user'] = self.request.user
        return initial

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form: Any) -> HttpResponse:
        form.article = self.get_object()
        form.user = self.request.user
        form.save()
        messages.success(self.request, _('Comment posted!'))
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('article_detail', kwargs={'pk':self.get_object().pk})