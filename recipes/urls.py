
from django.urls import path

from recipes.views import miss_marvel, visao

urlpatterns = [
    path('miss/', miss_marvel),
    path('visao/', visao),
]
