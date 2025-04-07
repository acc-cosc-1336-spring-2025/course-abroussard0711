import unittest

from src.homework.i_dictionaries_sets.dictionary import get_p_distance, get_p_distance_matrix

class Test_Config(unittest.TestCase):

    def test_p_distance (self):
        seq1 = ['T','T','T','C','C','A','T','T','T','A']
        seq2 = ['G','A','T','T','C','A','T','T','T','C']

        self.assertEqual (get_p_distance (seq1, seq2), 0.4)

    def test_get_p_distance_matrix (self):
        input_data = [
        ['T','T','T','C','C','A','T','T','T','A'],
        ['G','A','T','T','C','A','T','T','T','C'],
        ['T','T','T','C','C','A','T','T','T','T'],
        ['G','T','T','C','C','A','T','T','T','A']]

        expected_output = [
        [0.0, 0.4, 0.1, 0.1],
        [0.4, 0.0, 0.4, 0.3],
        [0.1, 0.4, 0.0, 0.2],
        [0.1, 0.3, 0.2, 0.0]]

        self.assertEqual (get_p_distance_matrix (input_data), expected_output)