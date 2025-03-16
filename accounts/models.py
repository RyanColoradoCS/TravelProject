from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    car_type = models.CharField(max_length=50, null=True, blank=True)
    
'''   
null=True:
Database Level: This means the database is allowed to store NULL values for this field. 
In other words, null=True allows the database column to be empty.

Use Case: It's typically used for non-string fields, such as numbers or dates. For string-based fields, it's more common to use an empty string "" instead of NULL.

blank=True:
Form Validation Level: This means the field is allowed to be empty in forms. It allows Django forms to accept
and validate empty inputs for this field.
'''