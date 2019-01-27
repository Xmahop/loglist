from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'loglists/index.html')
def posts(request):
    """Show all topics."""
    posts = Post.objects.order_by('-date_now')
    context = {'posts': posts}
    return render(request, 'loglists/topics.html', context)
