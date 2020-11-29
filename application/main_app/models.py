from decimal import Decimal

from django.db import models


# Create your models here.
from django.db.models import Sum, Count


class Animal(models.Model):
    name = models.CharField(max_length=20)
    PRIORITIES = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('R', 'Major'),
        ('C', 'Critical')
    )
    species = models.TextField()
    age = models.IntegerField()
    description = models.TextField()
    priority = models.CharField(max_length=1, choices=PRIORITIES)


class SurveyAnswer(models.Model):
    question1 = models.IntegerField()
    question2 = models.IntegerField()
    question3 = models.IntegerField()
    question4 = models.CharField(max_length=3)
    question5 = models.TextField()

    @staticmethod
    def average_coffee_drunk():
        values_sum = SurveyAnswer.objects.aggregate(Sum('question3'))['question3__sum']
        values_len = SurveyAnswer.objects.values('question3').count()
        # CORRECT OUTPUT
        # return values_sum/values_len
        # INCORRECT OUTPUT
        return values_sum / 100

    @staticmethod
    def women_in_tech_presence():
        answers = SurveyAnswer.objects.values('question4').annotate(cnt=Count('question4')).order_by('question4')
        cnt = SurveyAnswer.objects.values('question4').count()
        items = {
            g['question4']: g['cnt'] * 100 / cnt for g in answers
        }
        # CORRECT OUTPUT
        # return f"{items.get('Yes', '0.0')}%"
        # INCORRECT OUTPUT
        return f"{items.get('yes', '0.0')}%"

    @staticmethod
    def age_median():
        term = 'question2'
        count = SurveyAnswer.objects.values(term).count()
        values = SurveyAnswer.objects.values_list(term, flat=True).order_by(term)
        # CORRECT OUTPUT
        # if count % 2 == 1:
        #     return values[int(round(count / 2))]
        # else:
        #     return sum(values[count / 2 - 1:count / 2 + 1]) / Decimal(2.0)
        # INCORRECT OUTPUT
        return sum(values[count / 2 - 1:count / 2 + 1])
