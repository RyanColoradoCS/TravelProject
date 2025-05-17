from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView # A generic class-based view that displays a list of objects.
from django.contrib.auth.decorators import login_required
from .models import Post, UserPost, Profile
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
    
    is_logged_in_user = user_profile == request.user
    
    # Fetch posts by this user
    user_posts = UserPost.objects.filter(author=user_profile).order_by('-created_at')

    # Handle search functionality
    query = request.GET.get('q')
    users = CustomUser.objects.filter(username__icontains=query) if query else None

    return render(request, 'profile.html', {'user': user_profile, 'user_posts': user_posts,'users': users, 'query': query, 'MEDIA_URL': settings.MEDIA_URL, 'is_logged_in_user': is_logged_in_user})

@login_required
def edit_post(request, pk):
    
    # Retrieve the post being edited
    user_post = get_object_or_404(UserPost, pk=pk)

    # Ensure only the author can edit the post
    if user_post.author != request.user:
        return redirect('profile_view', pk=request.user.pk)

    if request.method == 'POST':
        # Update post with form data
        user_post.title = request.POST.get('title')
        user_post.content = request.POST.get('content')
        user_post.save()
        # Redirect to profile page after saving
        #return redirect('profile_view', pk=request.user.pk)
        return redirect('userprofile_view', pk=user_post.author.pk)
    
    # Render the edit form prefilled with post data
    return render(request, 'edit_post.html', {'user_post': user_post})

@login_required
def delete_post(request, pk):
    
    # Retrieve the post being edited
    user_post = get_object_or_404(UserPost, pk=pk)

    # Ensure only the author can edit the post
    if user_post.author != request.user:
        return redirect('profile_view', pk=request.user.pk)

    if request.method == 'POST':
        # Update post with form data
        user_post.delete()
        # Redirect to profile page after saving
        #return redirect('profile_view', pk=request.user.pk)
        return redirect('profile_view', pk=user_post.author.pk)
    
    # Render the edit form prefilled with post data
    return render(request, 'delete_post.html', {'user_post': user_post})


@login_required
def userprofile_view(request, pk=None):
    # Get the user of the profile in the link
    user_profile = get_object_or_404(Profile, user__pk=pk) if pk else request.user.profile
    logger.error(f"Accessed Profile: {user_profile.user.username}, ID: {user_profile.user.id}")
    
    # Ge the user object of the logged in user
    current_user = request.user
    logger.error(f"User object: {current_user}, ID: {current_user.id}")

    # check if profile is that of the logged in user or someone else
    is_logged_in_user = current_user == user_profile.user
    logger.error(f"Profile same as user? {is_logged_in_user}")

    # Fetch posts by this user of this profile
    # old code: user_posts = UserPost.objects.filter(author=user_profile).order_by('-created_at')
    user_posts = UserPost.objects.filter(author=user_profile.user).order_by('-created_at')

    # Handle search functionality
    query = request.GET.get('q')
    users = CustomUser.objects.filter(username__icontains=query) if query else None
    # possibly better: users = CustomUser.objects.filter(username__icontains=query) if query else CustomUser.objects.none()


    return render(request, 'profile.html', {
        'profile': user_profile,
        'user_posts': user_posts,
        'users': users,
        'query': query,
        'MEDIA_URL': settings.MEDIA_URL,
        'is_logged_in_user': is_logged_in_user,
    })
