import unittest

from algorithms.countingSort import countingSort

class countingSortTest(unittest.TestCase):

    def test_positive_numbers(self):
        input_array = [3, 4, 8, 7]
        result = [([3, 4, 7, 8], 2, -1, 3, -1),([3, 4, 7, 8], 3, -1, 2, -1),([3, 4, 7, 8], 1, -1, 1, -1),([3, 4, 7, 8], 0, -1, 0, -1)]
        sorting_result = list(countingSort(input_array))
        self.assertEqual(result, sorting_result)
        
        
        

    def test_combined_numbers(self):
        input_array = [8, 0, 13, 2]
        result = [([0, 2, 8, 13], 1, -1, 3, -1), ([0, 2, 8, 13], 3, -1, 2, -1), ([0, 2, 8, 13], 0, -1, 1, -1), ([0, 2, 8, 13], 2, -1, 0, -1)]
        sorting_result = list(countingSort(input_array))
        self.assertEqual(result, sorting_result)
        
        
        
    def test_equal_numbers(self):
        input_array = [3, 3, 3, 3]
        result = [([3, 3, 3, 3], 3, -1, 3, -1),([3, 3, 3, 3], 2, -1, 2, -1),([3, 3, 3, 3], 1, -1, 1, -1),([3, 3, 3, 3], 0, -1, 0, -1)]
        sorting_result = list(countingSort(input_array))
        self.assertEqual(result, sorting_result)
        
        
        
    def test_reverse_array(self):
        input_array = [8, 4, 3, 1]
        result = [([1, 3, 4, 8], 0, -1, 3, -1), ([1, 3, 4, 8], 1, -1, 2, -1), ([1, 3, 4, 8], 2, -1, 1, -1), ([1, 3, 4, 8], 3, -1, 0, -1)]
        sorting_result = list(countingSort(input_array))
        self.assertEqual(result, sorting_result)
        
        
        
        