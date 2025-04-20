import unittest
'''
the file in /tests/homework/j_classes/class_a
has the test class_a
'''
from tests.homework.j_classes import tests_classes

suite = unittest.TestLoader().loadTestsFromModule(tests_classes)
unittest.TextTestRunner(verbosity=2).run(suite)


