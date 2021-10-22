import unittest

import sys
sys.path.append("C:/Users/siris/Desktop/Master's/1st Semester/Software Engineering/Algorithms-Visualizer/src/main/python/algorithms")

from algorithms.bubbleSort import bubbleSort

class bubbleSortTest(unittest.TestCase):
    def testCasel(self):
        sample_input = [9, 3, 2, 4]
        expected_output = [([2, 3, 4, 9], 0, 1, -1, -1), ([2, 3, 4, 9], 1, 2, -1, -1), ([2, 3, 4, 9], 2, 3, -1, -1), ([2, 3, 4, 9], 0, 1, -1, -1), ([2, 3, 4, 9], 1, 2, -1, -1), ([2, 3, 4, 9], 0, 1, -1, -1)]
        res = list(bubbleSort(sample_input))
        #print (res)
        self.assertEqual(expected_output, res)
