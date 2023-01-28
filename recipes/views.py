from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Home(request):
    return render(request, 'recipes/home.html', context={'name': 'Arthur'})


def Contact(request):
    return HttpResponse('(62)98436-8603')


def About(request):
    return HttpResponse('Somos uma empresa criada em 2008...')
