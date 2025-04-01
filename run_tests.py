import unittest
'''
the file in /tests/homework/g_lists_and_tuples/tests_lists_and_tuples
has the test lists_and_tuples
'''
from tests.examples.i_dictionaries_sets import tests_dictionaries_and_sets

suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets)
unittest.TextTestRunner(verbosity=2).run(suite)


