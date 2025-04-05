from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView # A generic class-based view that displays a list of objects.
from django.contrib.auth.decorators import login_required
from .models import Post, UserPost
import logging
from accounts.models import CustomUser
from .forms import PostForm


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

@login_required
def feed_view(request):
    posts = UserPost.objects.all().order_by('-created_at')
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

    # Handle search functionality
    query = request.GET.get('q')
    users = CustomUser.objects.filter(username__icontains=query) if query else None

    return render(request, 'profile.html', {'user': user_profile, 'users': users, 'query': query})
