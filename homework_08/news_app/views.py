from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News

class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'

class NewsDetailView(DetailView):
    model = News
    template_name = 'news_detail.html'