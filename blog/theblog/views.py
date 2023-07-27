from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from django.contrib.auth.models import User
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from blog.utils import analyze_user_body
import nltk

# Create your views here.

#def home(request):
#    return render(request, 'home.html', {})



class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'articles.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatepost.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletepost.html'

    def get_success_url(self):
        return reverse_lazy('home')

class AnalyzePostView(DetailView):
    model = Post
    template_name = 'analysisresults.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        analysis_result = analyze_user_body(self.object.body)
        context['analysis_result'] = analysis_result
        return context


    
