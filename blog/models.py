from django.db import models
from django.conf import settings
from accounts.models import CustomUser
from django.utils.timezone import now

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
    
    title = models.CharField(max_length=255, default="Untitled Post", null=False, blank=False)  # Ensures it's always required
    # If the user is deleted, all their posts will also be deleted.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)  # Use this for creation time
    edited_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"
    
    def get_absolute_url(self):
        return reverse("userpost_detail", kwargs={"pk": self.pk})
    
class Profile(models.Model):
    
    '''
    OneToOneField is a type of foreign key in Django. However, it enforces a one-to-one relationship between two models, 
    rather than the many-to-one relationship that a regular ForeignKey allows.
    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Add optional profile details
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg', null=True, blank=True)
    website = models.URLField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
   
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    def get_absolute_url(self):
        return reverse("profile_detail", kwargs={"pk": self.pk})

# TODO: Future improvements for UserPost model
# - Add a `slug` field for SEO-friendly URLs and modify `get_absolute_url` accordingly.
# - Implement a `likes` field to allow user interactions with posts.
# - Consider adding a comment system for discussions.
# - Improve content validation to enforce length restrictions properly.
# - Ensure proper permissions and ownership checks in views.
# - Explore additional metadata fields (tags, categories, etc.).
