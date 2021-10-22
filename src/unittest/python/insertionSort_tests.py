import unittest

import sys
sys.path.append("C:/Users/siris/Desktop/Master's/1st Semester/Software Engineering/Sorting-Algorithms-Visualizer-master")

from algorithms.insertionSort import insertionSort

array = [3, 5, 2]

class InsertionSortTest(unittest.TestCase):
    def testCasel(self):
        input_array = array
        expected_output = [2, 3, 5]
        #expected_output = [([2, 3, 5], 1, -1, 2, -1),([2, 3, 5], 0, -1, 2, -1)]
        print ("Input: ", input_array)
        list(insertionSort(array))
        print ("Output: ", array)
        self.assertEqual(expected_output, array)
