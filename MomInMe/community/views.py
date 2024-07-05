# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Assign the current user to the post
            post.save()
            return redirect('community')  # Redirect to feed page after successful creation
    else:
        form = PostForm()
    
    return render(request, 'post_create.html', {'form': form})

# def feed(request):
#     posts = Post.objects.all().order_by('-created_at')
#     return render(request, 'feed.html', {'posts': posts})

def community(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'community.html', {'posts': posts})

@login_required
def post_update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('community')  # Redirect to community page after successful update
    else:
        form = PostForm(instance=post)
    
    return render(request, 'post_update.html', {'form': form, 'post': post})