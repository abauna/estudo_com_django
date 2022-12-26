from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe
from .utils.recipes.factory import make_recipe


# Create your views here.
def recipes(request, id):

    recipe = get_object_or_404(Recipe,        pk=id,
                               is_published=True,)
    return render(request, 'page/recipe.html', context={
        'recipe': recipe,
        'detail_page': True,
    })


def recipe(request):

    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    recipes = get_list_or_404(
        Recipe.objects.filter(
            is_published=True
        ).order_by('-id')
    )
    return render(request, 'page/home.html', context={
        'recipes': recipes,
        'detail_page': False
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')
    if not recipes:
        raise HttpResponse(content='not found', status=404)

    return render(request, 'page/category.html', context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name}'
    })
