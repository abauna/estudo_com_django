
from django.core.paginator import Paginator
from django.db.models import Q
from django.http.response import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe
from .utils.pages import make_pagination_range


# Create your views here.
def recipes(request, id):

    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)
    return render(request, 'page/recipe.html', context={
        'recipe': recipe,
        'detail_page': True,
    })


def recipe(request):
    recipes = Recipe.objects.filter(
        is_published=True,
    ).order_by('-id')

    try:
        page_atual = int(request.GET.get('page', 1))
    except ValueError:
        page_atual = 1
    paginator = Paginator(recipes, 9)
    page_o = paginator.get_page(page_atual)
    pagination_range = make_pagination_range(
        paginator.page_range,
        4,
        page_atual,

    )
    return render(request, 'page/home.html', context={
        'recipes': page_o,
        'detail_page': False,
        'pagination_range': pagination_range
    })


def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id'))

    return render(request, 'page/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name}- Category | '
    })


def search(request):

    search_term = request.GET.get('q', '').strip()
    if not search_term:
        raise Http404()
    recipes = Recipe.objects.filter(
        Q(
            Q(
                title__icontains=search_term
            ) |
            Q(
                description__icontains=search_term
            ),
            is_published=True
        )

    ).order_by('-id')
    recipes = recipes.filter(is_published=True)
    return render(request, 'page/search.html',
                  {
                      'page_title': f'Search for "{search_term}" |',
                      'search_term': search_term,
                      'recipes': recipes
                  })
