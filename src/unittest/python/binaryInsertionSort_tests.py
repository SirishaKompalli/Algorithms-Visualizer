import unittest
from algorithms.binaryinsertionSort import binaryinsertionSort

class BinaryInsertionSortTest(unittest.TestCase):
	def testCase1(self):
		sample_input = [13, 1]
		expected_output = [([1, 13], 0, 0, 0, 1)]
		res = list(binaryinsertionSort(sample_input))
		self.assertEqual(expected_output, res)

	def testCase2(self):
		sample_input = []
		expected_output = []
		res = list(binaryinsertionSort(sample_input))
		self.assertEqual(expected_output, res)

	def testCase3(self):
		sample_input = [13, 1, 99]
		expected_output = [([1, 13, 99], 0, 0, 0, 1), ([1, 13, 99], 0, 1, 2, 2)]
		res = list(binaryinsertionSort(sample_input))
		self.assertEqual(expected_output, res)

	def testCase4(self):
		sample_input = [13, 17]
		expected_output = [([13, 17], 0, 0, 1, 1)]
		res = list(binaryinsertionSort(sample_input))
		self.assertEqual(expected_output, res)
