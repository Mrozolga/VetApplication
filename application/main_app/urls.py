from django.urls import path
from .views import hello_world, survey_preview, add_answer, surveys_analytics

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('add_answer', add_answer, name="add_answer"),
    path('survey_preview', survey_preview, name="survey_preview"),
    path('surveys_analytics', surveys_analytics, name="surveys_analytics"),
]