from django.urls import path
from .views import hello_world, animals_list, add_answer, surveys_analytics

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('add_answer', add_answer, name="add_answer"),
    path('animals_list', animals_list, name="animals_list"),
    path('surveys_analytics', surveys_analytics, name="surveys_analytics"),
]