from django.urls import path 
# Import the path function, which is used to define URL patterns.#
from .views import BlogListView, BlogDetailView,feed_view, edit_post, delete_post, userprofile_view

# Define the URL patterns for the blog app
urlpatterns = [
    # Map the root URL of the blog app to the BlogListView
    # This will call the as_view() method on BlogListView to generate the appropriate response
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path("blog/", BlogListView.as_view(), name="blog"),
    path('feed/', feed_view, name='feed'),
    # path('myprofile/', profile_view, name='myprofile'),
    # path('profile/<int:pk>/', profile_view, name='user_profile'), # View other users' profiles
    # path('profile/<int:pk>/', profile_view, name='profile_view'),
    path('edit_post/<int:pk>/', edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', delete_post, name='delete_post'),
    # test
    path('userprofile/<int:pk>/', userprofile_view, name='userprofile_view'),

]


