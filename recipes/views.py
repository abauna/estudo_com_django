from django.http import HttpResponse
from django.shortcuts import render

from .utils.recipes.factory import make_recipe


# Create your views here.
def recipes(request, id):
    return render(request, 'page/recipe.html',
                  context={'recipe': make_recipe(),
                           'detail_page': True
                           })


def recipe(request):
    return render(request, 'page/home.html', context={
        'recipes': [make_recipe() for _ in range(3)],
    })
