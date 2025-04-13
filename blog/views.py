from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView # A generic class-based view that displays a list of objects.
from django.contrib.auth.decorators import login_required
from .models import Post, UserPost
import logging
from accounts.models import CustomUser
from .forms import PostForm
from django.conf import settings



logger = logging.getLogger(__name__)

# Create your views here.
# this is class based view instead of funtion based view

class BlogListView(ListView):
    model = Post # Specifies the model to use. In this case, Post is the model whose objects will be listed.
    # template_name = "home.html"  Specifies the template to use for rendering the list. 
    # In this case, home.html is the template file where the list of posts will be displayed.
    template_name = "blog.html" 

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

# TODO: Future improvements for feed_view
# - Implement pagination to efficiently display posts without loading everything at once.
# - Improve error handling to provide clearer messages when post creation fails.
# - Use POST-Redirect-GET (PRG) pattern to prevent accidental form resubmission.
# - Consider adding user notifications or feedback when new posts are created.
# - Explore options for filtering or sorting posts based on categories or user preferences.

@login_required
def feed_view(request):
    #posts = UserPost.objects.all().order_by('-created_at')
    posts = UserPost.objects.exclude(author=request.user).order_by('-created_at')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'feed.html', {'posts': posts, 'form': form})



@login_required
def profile_view(request, pk=None):
    # Determine the profile to show
    user_profile = get_object_or_404(CustomUser, pk=pk) if pk else request.user
    
    # Fetch posts by this user
    user_posts = UserPost.objects.filter(author=user_profile).order_by('-created_at')

    # Handle search functionality
    query = request.GET.get('q')
    users = CustomUser.objects.filter(username__icontains=query) if query else None

    return render(request, 'profile.html', {'user': user_profile, 'user_posts': user_posts,'users': users, 'query': query, 'MEDIA_URL': settings.MEDIA_URL})

