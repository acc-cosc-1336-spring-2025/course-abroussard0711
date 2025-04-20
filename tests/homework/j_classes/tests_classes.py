#

import unittest

from src.homework.j_classes.class_a import Die

class Test_Config(unittest.TestCase):

    def test_die (self):

        die = Die ()

        for _ in range (3):
            die.roll ()
            value = die.get_rolled_value ()
            self.assertGreaterEqual (value, 1)
            self.assertLessEqual (value, 6)