from django.shortcuts import render


# Create your views here.
def Home(request):
    return render(request, 'recipes/home.html', context={'name': 'Arthur'})

