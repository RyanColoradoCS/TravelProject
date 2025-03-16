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



class GoogleMapsData(models.Model):
    
    location_name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    # Add other fields as needed


class Locations(models.Model):
    club = models.CharField(max_length=500,blank=True, null=True)
    name = models.CharField(max_length=500)
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    country = models.CharField(max_length=200,blank=True, null=True)
    adress = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    edited_at = models.DateTimeField(auto_now=True)

    lat = models.CharField(max_length=200,blank=True, null=True)
    lng = models.CharField(max_length=200,blank=True, null=True)
    place_id = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return self.name


class Trip(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_coord = models.CharField(max_length=255)
    end_coord = models.CharField(max_length=255)
    whatever_api_spits_out = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Trip {self.id} for {self.user.email}"

class Location(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='locations')
    # Name of stop?
    long = models.FloatField() # This will eventually be gotten from API
    lat = models.FloatField() # This will eventually be gotten from API
    stop_type = models.CharField(max_length=20)
    stop_order = models.PositiveIntegerField(default=1)  # Field to indicate the order of stops
    # User notes - got gas for whatever
    
    class Meta:
        ordering = ['stop_order']
        unique_together = ('trip', 'stop_order')  # Enforce uniqueness for stop_order per trip
    
    '''
    When you set the ordering attribute in the Meta class, you're instructing Django to order the results 
    of any queries on this model by the specified field(s). This doesn't change how the data is stored in 
    the database; it only affects how the data is returned when queried.
    
    When you query the Location model, Django automatically adds an ORDER BY stop_order clause to the 
    SQL query it generates. This means the results are retrieved from the database in the order 
    specified by the stop_order field.
    
    Without Meta: You'd need to manually order your queries and enforce unique constraints in your application 
    logic, which can lead to repetitive and error-prone code.

    With Meta: Django handles these aspects for you, reducing redundancy and potential errors.
    
    '''
    
    def __str__(self):
        return f"Location {self.id} for Trip {self.trip.id}"
