from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AnalyzePostView, ResourcesView

urlpatterns = [

    path('', views.original, name='original'),
    path('home', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='articles'),
    path('addpost/', AddPostView.as_view(), name='addpost'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='updatepost'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='deletepost'),
    path('analyze/<int:pk>/', AnalyzePostView.as_view(), name='analysisresults'),
    path('resources/<int:pk>/', ResourcesView.as_view(), name='resources'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
