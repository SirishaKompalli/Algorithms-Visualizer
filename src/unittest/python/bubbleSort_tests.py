import unittest
from algorithms.bubbleSort import bubbleSort

class BubbleSortTest(unittest.TestCase):
	def testCase1(self):
		sample_input = [1, 125, 34, 12]
		expected_output = [1, 12, 34, 125]
		res = list(bubbleSort(sample_input))[0][0]
		self.assertEqual(expected_output, res) 