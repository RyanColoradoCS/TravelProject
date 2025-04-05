from django.db import models
from django.conf import settings
from accounts.models import CustomUser 

# Import the reverse function to create URLs by reversing the URL patterns
from django.urls import reverse

# Define the Post model
class Post(models.Model):
    # Title of the blog post
    title = models.CharField(max_length=200)
    # Author of the post, linked to Django's built-in User model
    # This needs to change to custom User model later
    # on_delete=models.CASCADE means if the user is deleted, the related posts will also be deleted
    # author = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # Use settings.AUTH_USER_MODEL
    # Body of the blog post
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    # String representation of the Post model, used in the admin interface
    def __str__(self):
        return self.title
    
    # Get the URL for the post detail view
    '''
    get_absolute_url method in the Post model is used to provide the canonical URL for a specific instance 
    of the model. In other words, it helps to generate a URL that points to a specific post detail view.
    '''
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

class UserPost(models.Model):
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"
    
    def get_absolute_url(self):
        return reverse("userpost_detail", kwargs={"pk": self.pk})
