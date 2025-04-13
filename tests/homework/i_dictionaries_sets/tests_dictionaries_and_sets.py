import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_widget_inventory

class Test_Config(unittest.TestCase):

    def test_add_inventory (self):

        inventory = {}

        add_inventory (inventory, 'Widget1', 10)
        self.assertEqual (inventory ['Widget1'], 10)

        add_inventory (inventory, 'Widget1', 25)
        self.assertEqual (inventory ['Widget1'], 35)

        add_inventory (inventory, 'Widget1', -10)
        self.assertEqual (inventory ['Widget1'], 25)

def test_remove_widget_inventory(self):
        inventory = {'Widget1': 10,'Widget2': 20}

        result = remove_widget_inventory(inventory, 'Widget1')
        self.assertEqual(result, "Record deleted")
        self.assertEqual(len(inventory), 1)
        self.assertIn('Widget2', inventory)
        self.assertNotIn('Widget1', inventory)
