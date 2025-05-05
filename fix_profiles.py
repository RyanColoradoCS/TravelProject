import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')  # Adjusted to match your project structure
django.setup()

from django.contrib.auth import get_user_model
from blog.models import Profile

User = get_user_model()

def create_missing_profiles():
    users_without_profiles = User.objects.filter(profile__isnull=True)
    for user in users_without_profiles:
        Profile.objects.create(user=user)
        print(f"Created profile for user: {user.username}")

if __name__ == "__main__":
    create_missing_profiles()