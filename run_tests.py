import unittest
'''
the file in /tests/examples/d_repetition/tests_repetition
has the test functions
'''
from tests.examples.d_repetition import tests_repetition

suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
unittest.TextTestRunner(verbosity=2).run(suite)
