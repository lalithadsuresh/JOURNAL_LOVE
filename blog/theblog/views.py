from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from django.contrib.auth.models import User
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from blog.utils import detect_emotions
from blog.utils import response_text, randomize_texts, sentiment_response, sentiment_analysis, process_negative_text, process_positive_text, analyze_sentence_structure
from blog.utils import get_synonyms, get_synonyms_for_list, fafo 
from django.shortcuts import render


# Create your views here.   

#def home(request):
#    return render(request, 'home.html', {})




def original(request):
    return render(request, 'index.html')

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

class ResourcesView(DetailView):
    model = Post
    template_name = 'resources.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AnalyzePostView(DetailView):
    model = Post
    template_name = 'analysisresults.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        emotions = detect_emotions(self.object.body)
        text1 = sentiment_response(self.object.body)
        synonyms = get_synonyms_for_list(emotions)
        poslist = fafo(emotions)
        analysis_result = response_text(emotions)
        context['analysis_result'] = analysis_result
        context['text1'] = text1
        context['poslist'] = poslist
        #context['synonyms'] = synonyms
        #context['text'] = text
        
        return context



    
