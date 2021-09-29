from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Articles


class ArticleListView(ListView):
    model = Articles
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Articles
    template_name = "article_detail.html"


class ArticleUpdateView(UpdateView):
    model = Articles
    template_name = "article_update.html"


class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
