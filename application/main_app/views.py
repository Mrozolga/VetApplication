from django.shortcuts import render
from .models import SurveyAnswer


def hello_world(request):
    return render(request, 'survey.html', {})


def add_answer(request):
    # try:
    if request.method == 'POST':
        survey = SurveyAnswer()
        survey.question1 = request.POST.get('question1')
        survey.question2 = request.POST.get('question2')
        survey.question3 = request.POST.get('question3')
        survey.question4 = request.POST.get('question4')
        survey.question5 = request.POST.get('question5')
        survey.save()

        return render(request, 'survey.html', {})

    else:
        return render(request, 'survey.html', {})


def survey_preview(request):
    model = SurveyAnswer
    questions_mapping = {
        "question1": "1. How do you like the weather today?",
        "question2": "2. What is your age?",
        "question3": "3. How many coffees did you drink today?",
        "question4": "4. Is it your first Women in Tech Conference?",
        "question5": "5. How would you name your boat if you had one?"
    }
    field_names = [f.name for f in model._meta.get_fields() if f.name != "id"]
    data = [[getattr(ins, name) for name in field_names]
            for ins in model.objects.prefetch_related().all()]
    return render(request, 'survey_preview.html', {'field_names': [questions_mapping.get(x) for x in field_names], 'data': data})


def surveys_analytics(request):
    model = SurveyAnswer()
    avg = model.average_coffee_drunk()
    wit_presence = model.women_in_tech_presence()
    age_median = model.age_median()
    return render(request, 'surveys_analytics.html', {'coffee_avg': avg, 'wits_presence': wit_presence,
                                                      'age_median': age_median})
