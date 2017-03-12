from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from .models import Article


def home(request):
    numbers_list = range(1, 1000)

    page = request.GET.get('page', 1)

    paginator = Paginator(numbers_list, 20)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    return render(request, 'blog/home.html', {'numbers': numbers})


class ArticlesView(ListView):
    model = Article
    paginate_by = 5
    context_object_name = 'articles'
    template_name = 'blog/articles.html'


def generate_fake_data(request):
    from model_mommy import mommy
    mommy.make('blog.Article', _quantity=20)
    return redirect('blog')
