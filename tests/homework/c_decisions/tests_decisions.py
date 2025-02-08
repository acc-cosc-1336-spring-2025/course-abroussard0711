#to test the get_options_ratio and get_faculty_rating decision functions

import unittest

from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_get_options_ratio (self):
        # to test the function get_options_ratio returns .25
        self.assertEqual(get_options_ratio(5,20),.25)

        # to test the function get_options_ratio returns .5
        self.assertEqual (get_options_ratio(10,20), .5)

    def test_get_faculty_rating (self):
        # to test the function get_faculty_rating returns ‘Excellent’ when the rating is .91
        self.assertEqual (get_faculty_rating(.91), 'Excellent')

        # to test the function get_faculty_rating returns ‘Very Good’ when the rating is .85
        self.assertEqual (get_faculty_rating (.85), 'Very Good') 

        # to test the function get_faculty_rating returns ‘Good’ when the rating is .71
        self.assertEqual (get_faculty_rating (.71), 'Good')

        # to test the function get_faculty_rating returns ‘Needs Improvement’ when the rating is .66
        self.assertEqual (get_faculty_rating (.66), 'Needs Improvement')

        # to test the function get_faculty_rating returns ‘Unacceptable’ when the rating is .45
        self.assertEqual (get_faculty_rating (.45), 'Unacceptable')

