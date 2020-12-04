from decimal import Decimal

from django.db import models


# Create your models here.
from django.db.models import Sum, Count


class SurveyAnswer(models.Model):
    question1 = models.IntegerField()
    question2 = models.IntegerField()
    question3 = models.IntegerField()
    question4 = models.CharField(max_length=3)
    question5 = models.TextField()

    @staticmethod
    def average_coffee_drunk():
        # sum all of the values from database (cups of coffee)
        sum_of_all_coffees_drunk = SurveyAnswer.objects.aggregate(Sum('question3'))['question3__sum']
        # count returns number of items in database
        count = SurveyAnswer.objects.values('question3').count()
        return SurveyAnswer.count_average(sum_of_all_coffees_drunk, count)

    @staticmethod
    def women_in_tech_presence():
        # get all of the values from database with their counters
        answers = SurveyAnswer.objects.values('question4').annotate(cnt=Count('question4')).order_by('question4')
        # count returns number of items in database
        count = SurveyAnswer.objects.values('question4').count()
        return SurveyAnswer.get_percentage_of_attendance(answers, count)

    @staticmethod
    def age_median():
        term = 'question2'
        count = SurveyAnswer.objects.values(term).count()
        if not count:
            return 0
        values = SurveyAnswer.objects.values_list(term, flat=True).order_by(term)
        return SurveyAnswer.count_median(values, count)

    @staticmethod
    def count_median(list_of_values: list, count: int) -> int:
        if len(list_of_values) == 0:
            return 0
        # CORRECT OUTPUT
        # if count % 2 == 1:
        #     return list_of_values[int(round(count / 2))]
        # else:
        #     index = int(count/2)
        #     return sum(list_of_values[index-1:index + 1]) / 2.0

        # INCORRECT OUTPUT
        if count % 2 == 1:
            return list_of_values[int(round(count / 2))]
        else:
            index = int(count / 2)
            return sum(list_of_values[index - 1:index + 1]) / 3.0

    @staticmethod
    def get_percentage_of_attendance(dict_of_attendance: list, count: int) -> str:
        if not count:
            return '0.0%'
        items = {
            g['question4']: round(g['cnt'] * 100 / count, 2) for g in dict_of_attendance
        }
        # CORRECT OUTPUT
        # return f"{items.get('Yes', '0.0')}%"

        # INCORRECT OUTPUT
        return f"{items.get('yes', '0.0')}%"

    @staticmethod
    def count_average(sum_of_all_coffees_drunk: int, count: int) -> float:
        if not sum_of_all_coffees_drunk:
            return 0.0
        # CORRECT OUTPUT
        # return round(sum_of_all_coffees_drunk/count, 2)

        # INCORRECT OUTPUT
        return sum_of_all_coffees_drunk / 100
