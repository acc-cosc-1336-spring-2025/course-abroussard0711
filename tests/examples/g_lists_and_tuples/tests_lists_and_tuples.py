import unittest

from src.examples.g_lists_and_tuples.lists import test_config, list_as_parameter, list_as_return_value, get_total_value_of_list_items_while, get_total_value_of_list_items_for

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_list_as_parameter(self):
        list1 = [5, 3, 10]
        print (' ')
        print (id(list[0]))

        expected_list = list1
        print (id(expected_list[0]))

        list_as_parameter (list1)

        self.assertEqual (list1[0], 100)
        self.assertEqual (list1, expected_list)
        
    def get_total_value_of_list_items_while(self):
        self.assertEqual (get_total_value_of_list_items_while(), 30)

    def get_total_value_of_list_items_for(self):
        self.assertEqual (get_total_value_of_list_items_for(), 30)


 #   def test_list_as_return_value (self):
 #       list1 = [5, 3, 10]
 #       print (' ')
 #       print ('test list2' + str(id(list1[0])))
#
  #      expected_list = list1
 #       print ('expected list' + str(id(expected_list[0])))
#
 #       return_list = list_as_return_value (list1)
 #       print ('test return_list' + str(id(return_list[0])))

 #       self.assertEqual (list1[0], return_list (list1))

    
    
