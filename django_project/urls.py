
from django.contrib import admin
from django.urls import path, include
from .views import home
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Admin URLs
    path('admin/', admin.site.urls),
    
    # App-specific URLs
    # This line includes the URL patterns defined in another module, in this case, blogs.urls
    path('', include("blog.urls")),  # Blog app at the root path
    path('accounts/', include("accounts.urls")),  # Custom account URLs
    path('accounts/', include("django.contrib.auth.urls")),  # Django's built-in auth
    
    path("", home, name="home"),  # Home page
    path("home/", home, name="home"),  # Home page
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# The `static()` function connects MEDIA_URL to MEDIA_ROOT,
# allowing media files to be displayed properly while running the Django development server.
# This is only used in development. In production, media files should be served by a web server like Nginx or Apache.