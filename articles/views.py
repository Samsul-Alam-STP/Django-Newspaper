from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Articles


class ArticleListView(ListView):
    model = Articles
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Articles
    template_name = "article_detail.html"


class ArticleUpdateView(UpdateView):
    model = Articles
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"


class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")


class ArticleCreateView(CreateView):
    model = Articles
    template_name = "article_new.html"
    fields = (
        "title",
        "author",
        "body",
    )
