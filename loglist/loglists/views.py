from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'loglists/index.html')
def posts(request):
    posts = Post.objects.order_by('date_now') #запрос к БД на получение всех posts отсортированных по дате
    context = {'posts': posts}
    b = Post.objects.all()
    a = b[0]
    return render(request, 'loglists/topics.html', context,a)
