from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    relationship_to_kinsey = models.CharField(max_length=100, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse("profile_link", kwargs={"pk": self.pk})

    
'''   
null=True:
Database Level: This means the database is allowed to store NULL values for this field. 
In other words, null=True allows the database column to be empty.

Use Case: It's typically used for non-string fields, such as numbers or dates. For string-based fields, it's more common to use an empty string "" instead of NULL.

blank=True:
Form Validation Level: This means the field is allowed to be empty in forms. It allows Django forms to accept
and validate empty inputs for this field.
'''