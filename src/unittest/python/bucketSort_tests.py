import unittest
from algorithms.bucketSort import bucketSort

class BogoSortTest(unittest.TestCase):
	def testCase1(self):
		sample_input = [3, 1]
		expected_output = [1, 3]
		res = list(bucketSort(sample_input))[0][0]
		self.assertEqual(expected_output, res)

	def testCase2(self):
		sample_input = []
		expected_output = []
		res = list(bucketSort(sample_input))
		self.assertEqual(expected_output, res)

	def testCase3(self):
		sample_input = [1, 2, 3, 4, 5]
		expected_output = [1, 2, 3, 4, 5]
		res = list(bucketSort(sample_input))[0][0]
		self.assertEqual(expected_output, res)

	def testCase4(self):
		sample_input = [13, 11, 29, 0, 12, 33]
		expected_output = [0, 11, 12, 13, 29, 33]
		res = list(bucketSort(sample_input))[0][0]
		self.assertEqual(expected_output, res)