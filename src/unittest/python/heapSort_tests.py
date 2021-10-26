import unittest

from algorithms.heapSort import heapSort

class heapSortTest(unittest.TestCase):

    def test_positive_numbers(self):
        input_array = [3, 8, 6]
        result = [([3, 6, 8], 0, 1, -1, -1), ([3, 6, 8], -1, -1, 0, 2), ([3, 6, 8], -1, -1, 0, 1)]
        sorting_result = list(heapSort(input_array))
        self.assertEqual(result, sorting_result)
        
        
    def test_negative_numbers(self):
        input_array = [-4, -7, -4]
        result = [([-7, -4, -4], -1, -1, 0, 2), ([-7, -4, -4], -1, -1, 0, 1)]
        sorting_result = list(heapSort(input_array))
        self.assertEqual(result, sorting_result)
        
        

    def test_combined_numbers(self):
        input_array = [8, -43, -1]
        result = [([-43, -1, 8], -1, -1, 0, 2), ([-43, -1, 8], -1, -1, 0, 1)]
        sorting_result = list(heapSort(input_array))
        self.assertEqual(result, sorting_result)
        
        
        
    def test_equal_numbers(self):
        input_array = [2, 2, 2]
        result = [([2, 2, 2], -1, -1, 0, 2), ([2, 2, 2], -1, -1, 0, 1)]
        sorting_result = list(heapSort(input_array))
        self.assertEqual(result, sorting_result)
        
        
        
    def test_reverse_array(self):
        input_array = [8, 4, -2]
        result = [([-2, 4, 8], -1, -1, 0, 2), ([-2, 4, 8], 0, 1, -1, -1), ([-2, 4, 8], -1, -1, 0, 1)]
        sorting_result = list(heapSort(input_array))
        self.assertEqual(result, sorting_result)
        
        

    def test_empty_array(self):
        input_array = []
        result = []
        sorting_result = list(heapSort(input_array))
        self.assertEqual(result, sorting_result)
        
        