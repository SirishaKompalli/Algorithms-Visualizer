import unittest
from algorithms.cocktailSort import cocktailSort

class BucketSortTest(unittest.TestCase):
	def testCase1(self):
		sample_input = [1, 125, 34, 12]
		expected_output = [1, 12, 34, 125]
		res = list(cocktailSort(sample_input))[0][0]
		self.assertEqual(expected_output, res)

	def testCase2(self):
		sample_input = []
		expected_output = []
		res = list(cocktailSort(sample_input))
		self.assertEqual(expected_output, res)