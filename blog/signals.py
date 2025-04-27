from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import Profile

'''
post_save is a built-in signal provided by Django that is triggered immediately 
after an object is saved to the database.

instance:
This is created by Django and represents the specific model instance that was just saved (e.g., a User object).

created:
This is created by Django and is a Boolean value
'''

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
