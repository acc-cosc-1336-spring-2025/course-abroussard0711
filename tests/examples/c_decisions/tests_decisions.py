import unittest

from src.examples.c_decisions.decisions import is_number_in_range, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def text_is_number_in_range(self):
        self.assertEqual(is_number_in_range(1,10,9),True)

    def test_is_vowel(self):
        self.assertEqual(is_number)

