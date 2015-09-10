from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# Import the Post model object from models.py
from .models import Post
# Import the PostForm model object from forms.py
from .forms import PostForm

# Create your views here.
def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
  if request.method == 'POST':
    form = PostForm(request.POST)
    if form.is_valid():
      # Save the post but do not commit them yet (i.e. commit=False)
      post = form.save(commit=False)
      post.author = request.user
      post.published_date = timezone.now()
      # Accept the changes and now commit them (i.e. commit=True/ save)
      post.save()
      # After saving new post successfully, redirect to new post detail view
      return redirect('blog.views.post_detail', pk=post.pk)
  else:
    form = PostForm()
  return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
  post = get_object_or_404(Post, pk=pk)
  if request.method == 'POST':
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.published_date = timezone.now()
      post.save()
      return redirect('blog.views.post_detail', pk=post.pk)
  else:
    form = PostForm(instance=post)
  return render(request, 'blog/post_edit.html', {'form': form})
