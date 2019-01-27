from django.shortcuts import render
from django.http import HttpResponse
from .models import Post #импортируем модель Post
from django.core.paginator import Paginator #пагинация

# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'loglists/index.html') #возвращает шаблон главной страницы
def posts(request, page_number=1):
    """Show all topics."""
    posts = Post.objects.order_by('-date_now') #получаем все объекты модели Post с сортировкой по времени
    paginator = Paginator(posts, 3) # создаем переменную типа Paginator и указываем что post должны отображаться по 15 на странице
    page = request.GET.get('page')
    all_post = paginator.get_page(page)
    #post_by_time = posts.order_by('-date_now')  #сортируем объекты модели Post по дате, вверху - последние
    context = {'all_post': all_post} #отгружаем словарь
    return render(request, 'loglists/topics.html', context) #возвращаем шаблон и словарь
