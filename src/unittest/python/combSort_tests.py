import unittest

from algorithms.combSort import combSort

class combSortTest(unittest.TestCase):

    def test_positive_numbers(self):
        input_array = [5, 4, 9]
        result = [([4, 5, 9], 0, 2, -1, -1), ([4, 5, 9], 0, 1, -1, -1), ([4, 5, 9], 1, 2, -1, -1), ([4, 5, 9], 0, 1, -1, -1), ([4, 5, 9], 1, 2, -1, -1)]
        sorting_result = list(combSort(input_array))
        self.assertEqual(result, sorting_result)
        
        
    def test_negative_numbers(self):
        input_array = [-2, -7, -4]
        result = [([-7, -4, -2], 0, 2, -1, -1), ([-7, -4, -2], 0, 1, -1, -1), ([-7, -4, -2], 1, 2, -1, -1), ([-7, -4, -2], 0, 1, -1, -1), ([-7, -4, -2], 1, 2, -1, -1)]
        sorting_result = list(combSort(input_array))
        self.assertEqual(result, sorting_result)
        
        

    def test_combined_numbers(self):
        input_array = [-8, 13, -12]
        result = [([-12, -8, 13], 0, 2, -1, -1), ([-12, -8, 13], 0, 1, -1, -1), ([-12, -8, 13], 1, 2, -1, -1), ([-12, -8, 13], 0, 1, -1, -1), ([-12, -8, 13], 1, 2, -1, -1)]
        sorting_result = list(combSort(input_array))
        #print(sorting_result)
        self.assertEqual(result, sorting_result)
        
        
        
    def test_equal_numbers(self):
        input_array = [5, 5, 5]
        result = [([5, 5, 5], 0, 2, -1, -1), ([5, 5, 5], 0, 1, -1, -1), ([5, 5, 5], 1, 2, -1, -1)]
        sorting_result = list(combSort(input_array))
        #print(sorting_result)
        self.assertEqual(result, sorting_result)
        
        
        
    def test_reverse_array(self):
        input_array = [8, 4, 2]
        result = [([2, 4, 8], 0, 2, -1, -1), ([2, 4, 8], 0, 1, -1, -1), ([2, 4, 8], 1, 2, -1, -1)]
        sorting_result = list(combSort(input_array))
        #print(sorting_result)
        self.assertEqual(result, sorting_result)
        
        

    def test_empty_array(self):
        input_array = []
        result = []
        sorting_result = list(combSort(input_array))
        self.assertEqual(result, sorting_result)