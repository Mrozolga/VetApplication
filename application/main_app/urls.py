from django.urls import path
from .views import hello_world, add_animal, animals_list

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('add_animal', add_animal, name="add_animal"),
    path('animals_list', animals_list, name="animals_list"),
]