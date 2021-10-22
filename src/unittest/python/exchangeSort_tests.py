import unittest

from algorithms.exchangeSort import exchangeSort

class exchangeSortTest(unittest.TestCase):

    def test_positive_numbers(self):
        input_array = [5, 4, 9]
        result = [([4, 5, 9], 0, 1, -1, -1), ([4, 5, 9], 0, 2, -1, -1), ([4, 5, 9], 1, 2, -1, -1)]
        sorting_result = list(exchangeSort(input_array))
        self.assertEqual(result, sorting_result)
        
        
    def test_negative_numbers(self):
        input_array = [-3, -9, -6]
        result = [([-9, -6, -3], 0, 1, -1, -1), ([-9, -6, -3], 0, 2, -1, -1), ([-9, -6, -3], 1, 2, -1, -1)]
        sorting_result = list(exchangeSort(input_array))
        self.assertEqual(result, sorting_result)
        
        

    def test_combined_numbers(self):
        input_array = [-6, 15, -7]
        result = [([-7, -6, 15], 0, 1, -1, -1), ([-7, -6, 15], 0, 2, -1, -1), ([-7, -6, 15], 1, 2, -1, -1)]
        sorting_result = list(exchangeSort(input_array))
        self.assertEqual(result, sorting_result)
        
        
        
    def test_equal_numbers(self):
        input_array = [9, 9, 9]
        result = [([9, 9, 9], 0, 1, -1, -1), ([9, 9, 9], 0, 2, -1, -1), ([9, 9, 9], 1, 2, -1, -1)]
        sorting_result = list(exchangeSort(input_array))
        self.assertEqual(result, sorting_result)
        
        
        
    def test_reverse_array(self):
        input_array = [13, 7, 1]
        result = [([1, 7, 13], 0, 1, -1, -1), ([1, 7, 13], 0, 2, -1, -1), ([1, 7, 13], 1, 2, -1, -1)]
        sorting_result = list(exchangeSort(input_array))
        self.assertEqual(result, sorting_result)
        
        

    def test_empty_array(self):
        input_array = []
        result = []
        sorting_result = list(exchangeSort(input_array))
        self.assertEqual(result, sorting_result)