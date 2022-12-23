from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def miss_marvel(request):
    return render(request, 'page/home.html', context={'name': 'abauna', })


def visao(request):
    return HttpResponse('wanda e visao')
