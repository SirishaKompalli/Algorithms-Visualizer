import unittest

from algorithms.gnomeSort import gnomeSort

class gnomeSortTest(unittest.TestCase):

    def test_positive_numbers(self):
        input_array = [15, 24, 99]
        result = [([15, 24, 99], 0, -1, -1, -1), ([15, 24, 99], 1, 0, -1, -1), ([15, 24, 99], 2, 1, -1, -1)]
        sorting_result = list(gnomeSort(input_array))
        self.assertEqual(result, sorting_result)
        
        
    def test_negative_numbers(self):
        input_array = [-3, -9, -8]
        result = [([-9, -8, -3], 0, -1, -1, -1), ([-9, -8, -3], 1, 0, -1, -1), ([-9, -8, -3], 0, -1, -1, -1), ([-9, -8, -3], 1, 0, -1, -1), ([-9, -8, -3], 2, 1, -1, -1), ([-9, -8, -3], 1, 0, -1, -1), ([-9, -8, -3], 2, 1, -1, -1)]
        sorting_result = list(gnomeSort(input_array))
        self.assertEqual(result, sorting_result)
        
        

    def test_combined_numbers(self):
        input_array = [-81, 12, -6]
        result = [([-81, -6, 12], 0, -1, -1, -1), ([-81, -6, 12], 1, 0, -1, -1), ([-81, -6, 12], 2, 1, -1, -1), ([-81, -6, 12], 1, 0, -1, -1), ([-81, -6, 12], 2, 1, -1, -1)]
        sorting_result = list(gnomeSort(input_array))
        self.assertEqual(result, sorting_result)
        
        
        
    def test_equal_numbers(self):
        input_array = [5, 5, 5]
        result = [([5, 5, 5], 0, -1, -1, -1), ([5, 5, 5], 1, 0, -1, -1), ([5, 5, 5], 2, 1, -1, -1)]
        sorting_result = list(gnomeSort(input_array))
        self.assertEqual(result, sorting_result)
        
        
        
    def test_reverse_array(self):
        input_array = [9, 4, -2]
        result = [([-2, 4, 9], 0, -1, -1, -1), ([-2, 4, 9], 1, 0, -1, -1), ([-2, 4, 9], 0, -1, -1, -1), ([-2, 4, 9], 1, 0, -1, -1), ([-2, 4, 9], 2, 1, -1, -1), ([-2, 4, 9], 1, 0, -1, -1), ([-2, 4, 9], 0, -1, -1, -1), ([-2, 4, 9], 1, 0, -1, -1), ([-2, 4, 9], 2, 1, -1, -1)]
        sorting_result = list(gnomeSort(input_array))
        self.assertEqual(result, sorting_result)
        
        

    def test_empty_array(self):
        input_array = []
        result = []
        sorting_result = list(gnomeSort(input_array))
        self.assertEqual(result, sorting_result)