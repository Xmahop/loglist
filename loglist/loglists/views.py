from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm #достаем из форм модель для формы нового поста
from django.core.paginator import Paginator #пагинация
from taggit.models import Tag
# Create your views here.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'loglists/index.html') #возвращает шаблон главной страницы
def posts(request, tag_slug=None):
    object_list = Post.objects.order_by('-date_now')
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    context = {'object_list': object_list,
                'tag': tag}
    return render(request, 'loglists/topics.html', context)


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
