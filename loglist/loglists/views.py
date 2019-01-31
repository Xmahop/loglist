from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post #импортируем модель Post
from .forms import PostForm #достаем из форм модель для формы нового поста
from django.core.paginator import Paginator #пагинация
# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'loglists/index.html') #возвращает шаблон главной страницы
def posts(request, page_number=1):
    """Show all topics."""
    posts = Post.objects.order_by('-date_now') #получаем все объекты модели Post с сортировкой по времени
    paginator = Paginator(posts, 5) # создаем переменную типа Paginator и указываем что post должны отображаться по 15 на странице
    page = request.GET.get('page')
    all_post = paginator.get_page(page)
    #post_by_time = posts.order_by('-date_now')  #сортируем объекты модели Post по дате, вверху - последние
    context = {'all_post': all_post} #отгружаем словарь
    return render(request, 'loglists/topics.html', context) #возвращаем шаблон и словарь


def new_post(request):
    if request.method != 'POST':
        form = PostForm()
        #Данные не отправлялись, создаем пустую форму
    else:
        #POST запрос, обрабатываем
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('loglists:posts'))
    context = {'form': form}
    return render(request, 'loglists/new_post.html', context)


def as_myp(self):
    "Returns this form rendered as HTML <p>s."
    return self._html_output(
        normal_row = '<p%(html_class_attr)s>%(label)s</p> <p>%(field)s%(help_text)s</p>',
        error_row = '%s',
        row_ender = '</p>',
        help_text_html = ' <span class="helptext">%s</span>',
        errors_on_separate_row = True)

def post(request, post_id):
    """Show a single topic, and all its entries."""
    post = get_object_or_404(Post, id=post_id)
    posst = Post.objects.order_by('-date_now')
    context = {'posst': posst}
    return render(request, 'loglists/post.html', context)


def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        form.is_valid()
        form.save()
        return HttpResponseRedirect(reverse('loglists:posts'))

    else:
        form = PostForm(instance = post)
    context = {'form': form,
                'post': post,
                }
    context = {'post':post,
                'form': form}

    return render (request, 'loglists/edit_post.html', context)
