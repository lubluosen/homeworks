from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import News

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'

class NewsCreateView(CreateView):
    model = News
    template_name = 'news/news_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)