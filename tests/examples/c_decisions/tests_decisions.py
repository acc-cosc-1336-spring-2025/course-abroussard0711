import unittest

from src.examples.c_decisions.decisions import get_generation, is_consonant, is_even, is_number_in_range, is_vowel, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def text_is_number_in_range(self):
        self.assertEqual(is_number_in_range(1,10,9),True)

    def test_is_vowel(self):
        self.assertEqual(is_vowel('a'), True)
        self.assertEqual(is_vowel('e'), True)
        self.assertEqual(is_vowel('i'), True)
        self.assertEqual(is_vowel('o'), True)
        self.assertEqual(is_vowel('u'), True)
        self.assertEqual(is_vowel('z'), False)

    def test_is_consonant (self):
        self.assertEqual(is_consonant('b'), True)
        self.assertEqual(is_consonant('a'), False)
        self.assertEqual(is_consonant('c'), True)
        self.assertEqual(is_consonant('e'), False)

    def test_is_even(self):
       self.assertEqual (is_even(3),False) #not even
       self.assertEqual (is_even(2),True) #even

    def test_get_generation(self):
        self.assertEqual(get_generation(1920),"The Greatest Generation")
        self.assertEqual(get_generation(1930),"The Silent Generation")
        self.assertEqual(get_generation(1950),"Baby Boomer Generation")
        self.assertEqual(get_generation(1970),"Generation X")
        self.assertEqual(get_generation(1985),"Generation Y")
        self.assertEqual(get_generation(2000),"Generation Z")
