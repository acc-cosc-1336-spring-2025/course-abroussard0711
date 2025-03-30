import unittest
'''
the file in /tests/homework/g_lists_and_tuples/tests_lists_and_tuples
has the test lists_and_tuples
'''
from tests.homework.g_lists_and_tuples import tests_lists_and_tuples

suite = unittest.TestLoader().loadTestsFromModule(tests_lists_and_tuples)
unittest.TextTestRunner(verbosity=2).run(suite)


