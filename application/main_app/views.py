from django.db.models import Model
from django.shortcuts import render
from .models import Animal
from django.http import HttpResponse


def hello_world(request):
    return render(request, 'hello_word.html', {})


def add_animal(request):
    if request.method == 'POST':
        animal = Animal()
        animal.name = request.POST.get('name')
        animal.species = request.POST.get('species')
        animal.age = request.POST.get('age')
        animal.priority = request.POST.get('priority')
        animal.description = request.POST.get('description')
        animal.save()

        return render(request, 'hello_word.html', {})

    else:
        return render(request, 'hello_word.html', {})


def animals_list(request):
    model = Animal
    field_names = [f.name for f in model._meta.get_fields()]
    data = [[getattr(ins, name) for name in field_names]
            for ins in model.objects.prefetch_related().all()]
    return render(request, 'animals_list.html', {'field_names': field_names, 'data': data})