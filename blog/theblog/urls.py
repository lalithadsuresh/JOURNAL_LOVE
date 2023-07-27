from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AnalyzePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='articles'),
    path('addpost/', AddPostView.as_view(), name='addpost'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='updatepost'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='deletepost'),
    path('analyze/<int:pk>/', AnalyzePostView.as_view(), name='analysisresults')
    

]
