import unittest
'''
the file in /tests/homework/h_strings/tests_strings
has the test strings
'''
from tests.homework.h_strings import tests_strings

suite = unittest.TestLoader().loadTestsFromModule(tests_strings)
unittest.TextTestRunner(verbosity=2).run(suite)


