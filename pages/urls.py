from .views import HomePageView
from django.urls import path

urlpatterns = [
    path("", HomePageView.as_view(template_name="home.html"), name="home"),  # Home page
    path("home/", HomePageView.as_view(template_name="home.html"), name="home"),  # Home page
    
]
