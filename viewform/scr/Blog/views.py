from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
        ListView,
        CreateView,
        DetailView,
        UpdateView,
        DeleteView
)
from .forms import ArticleModelForm
from .models import Article
#from Blog2.models import Product

# Create your views here.
class ArticleisView(ListView):
    template_name = 'Blog/article_list.html'
    queryset = Article.objects.all()               #<blog>/<modelname>_list.html

class ArticleCreateView(CreateView):
    template_name = 'Blog/article_create.html'
    form_class = ArticleModelForm
    #queryset = Article.objects.all()  #or success_url = '/'

    def form_valid(self, form):
        #print(form.cleaned_data)
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    template_name = 'Blog/article_detail.html'
    #queryset = Article.objects.all()       #queryset = Article.objects.filter(id__gt=1)

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)  #return Article.objects.get(id=id)


class ArticleUpdateView(UpdateView):
    template_name = 'Blog/article_create.html'
    form_class = ArticleModelForm
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'Blog/article_delete.html'
    #queryset = Article.objects.all()     #queryset = Article.objects.filter(id__gt=1)
    success_url = '../../'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    # def get_success_url(self):
    #     return reverse("Blog:article-list")

"""
success_url='../../' does the same job as ( def get_success_url(self): )
"""
