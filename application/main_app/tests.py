from django.test import TestCase
from .models import SurveyAnswer


class SurveyAnswerCase(TestCase):

    # def setUp(self):
    #     SurveyAnswer.objects.create(question1=1, question2=22, question3=3, question4="Yes", question5="Homelander")
    #     SurveyAnswer.objects.create(question1=2, question2=20, question3=1, question4="No", question5="Stark")
    #     SurveyAnswer.objects.create(question1=3, question2=28, question3=0, question4="No", question5="Aquaman")
    #     SurveyAnswer.objects.create(question1=3, question2=32, question3=1, question4="Maybe", question5="Harley")

    # MEDIAN UNIT TESTS

    def test_count_median_uneven(self):
        """
        This test checks if median is counted correctly when length of array is uneven.
        """
        sorted_list = [0, 1, 2, 5, 6]
        self.assertEqual(SurveyAnswer.count_median(sorted_list, len(sorted_list)), 2)

    def test_count_median_even(self):
        """
        This test checks if median is counted correctly when length of array is uneven.
        """
        sorted_list = [0, 1, 1, 5, 6, 10]
        self.assertEqual(SurveyAnswer.count_median(sorted_list, len(sorted_list)), 3)

    def test_count_median_on_0_elements(self):
        """
        This test checks if median is being returned when database is empty.
        """
        sorted_list = []
        self.assertEqual(SurveyAnswer.count_median(sorted_list, len(sorted_list)), 0)

    # AVERAGE UNIT TESTS

    def test_average(self):
        """
        This test checks if average is counted correctly.
        """
        list_of_weather_notes = [1, 4, 5, 2, 2, 3]
        sum_of_weather_notes = sum(list_of_weather_notes)
        self.assertEqual(SurveyAnswer.count_average(sum_of_weather_notes, len(list_of_weather_notes)), 2.83)

    def test_average_on_0_elements(self):
        """
        This test checks if average is counted correctly when database is empty.
        """
        list_of_weather_notes = []
        sum_of_weather_notes = sum(list_of_weather_notes)
        self.assertEqual(SurveyAnswer.count_average(sum_of_weather_notes, len(list_of_weather_notes)), 0.00)

    # WOMEN IN TECH ATTENDANCE

    def test_get_percentage_of_attendance(self):
        """
        This test checks if Women in Tech presence is counted correctly.
        """
        dict_of_attendance = [{
            'question4': 'Yes',
            'cnt': 70
        },
            {
                'question4': 'No',
                'cnt': 20
            },
            {
                'question4': 'Maybe',
                'cnt': 10
            }]
        count = 70 + 20 + 10
        self.assertEqual(SurveyAnswer.get_percentage_of_attendance(dict_of_attendance, count), '70.0%')

    def test_get_percentage_of_attendance_on_0_elements(self):
        """
        This test checks if Women in Tech presence is counted correctly when database is empty.
        """
        dict_of_attendance = []
        count = 0
        self.assertEqual(SurveyAnswer.get_percentage_of_attendance(dict_of_attendance, count), '0.0%')