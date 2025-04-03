import unittest

from src.examples.i_dictionaries_sets.dictionaries import test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_access_dictionary_value (self):
        phone_book = {'Chris':'999-7773', 'David':'555-2226'}

        self.assertEqual (phone_book ['Chris'], '999-7773')

    def test_invalid_key_access_dictionary (self):
        phone_book = {'Chris':'999-7773', 'David':'555-2226'}

        with self.assertRaises (KeyError):                      # this statement test that an error will exist resulting in a passed test
            phone_book ['Sam']                                  # it test that this key is NOT in the dictionary assigned in line 16

    def test_key_in_dictionary (self):
        phone_book = {'Chris':'999-7773', 'David':'555-2226'}

        self.assertEqual ('Katie' in phone_book, False)
        self.assertEqual ('Chris' in phone_book, True)

    def test_key_not_in_dictionary (self):
        phone_book = {'Chris':'999-7773', 'David':'555-2226'}

        self.assertEqual ('Katie' not in phone_book, True)
        self.assertEqual ('David' not in phone_book, False)

    def test_add_key_value_pair_dictionary (self):
        phone_book = {'Chris':'999-7773', 'David':'555-2226'}

        if 'Sam' not in phone_book:
            phone_book ['Sam'] = '888-2221'

        self.assertEqual (phone_book ['Sam'], '888-2221')


    def test_delete_key_value_pair_dictionary (self):
        phone_book = {'Chris':'999-7773', 'David':'555-2226', 'Sam':'888-2221'}

        if 'Sam' in phone_book:
            del phone_book ['Sam']

        self.assertEqual ('Sam' not in phone_book, True)

    def test_get_number_elements_in_dictionary (self):
        phone_book = {'Chris':'999-7773', 'David':'555-2226', 'Sam':'888-2221'}

        self.assertEqual (len(phone_book), 3)

    def test_dictionary_get (self):
        phone_book = {'Chris':'999-7773', 'David':'555-2226', 'Sam':'888-2221'}

        result = phone_book.get ('Sam', 'Key not found')
        self.assertEqual (result, '888-2221')

        result = phone_book.get ('Samm', 'Key not found')
        self.assertEqual (result, 'Key not found')

    def test_dictionary_items (self):
        phone_book = {'Chris':'999-7773', 'David':'555-2226', 'Sam':'888-2221'}
        list_tuple_items = phone_book.items()

        for key, value in phone_book.items():
            self.assertEqual (value, phone_book[key])

    
    def test_dictionary_pop_item (self):
        phone_book = {'Chris':'999-7773', 'David':'555-2226', 'Sam':'888-2221'}

        key, value = phone_book.popitem()

        self.assertEqual (key, 'Sam')
        self.assertEqual (value, '888-2221')
        self.assertEqual (phone_book, {'Chris':'999-7773', 'David':'555-2226'})