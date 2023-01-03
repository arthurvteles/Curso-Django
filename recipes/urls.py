from django.urls import path

from recipes.views import About, Contact, Home

urlpatterns = [
    path('', Home),
    path('contato/', Contact),
    path('sobre/', About),
]
