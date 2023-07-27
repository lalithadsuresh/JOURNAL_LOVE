from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    analysis_result = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')

    def analyze_user_body(user):
        # Get all the posts of the given user
        user_posts = Post.objects.filter(author=user)

        analysis_results = []
        for post in user_posts:
            body_length = len(post.body)
            
            # Store the analysis result in a list
            analysis_results.append({"post_id": post.id, "body_length": body_length})

        return analysis_results




        




# Create your models here.
