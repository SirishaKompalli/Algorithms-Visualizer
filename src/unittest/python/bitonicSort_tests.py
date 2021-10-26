import unittest
from algorithms.bitonicSort import bitonicSort

class BitonicSortTest(unittest.TestCase):
	def testCase1(self):
		sample_input = [13, 8, 99]
		expected_output = [([8, 13, 99], 0, -1, 1, -1)]
		res = list(bitonicSort(sample_input))
		self.assertEqual(expected_output, res)

	def testCase2(self):
		sample_input = [72, 8]
		expected_output = [([8, 72], 0, -1, 1, -1)]
		res = list(bitonicSort(sample_input))
		self.assertEqual(expected_output, res)

	def testCase3(self):
		sample_input = []
		expected_output = []
		res = list(bitonicSort(sample_input))
		self.assertEqual(expected_output, res)

	# def oneNumber_testCase(self):
	# 	sample_input = [13]
	# 	expected_output = [13]
	# 	res = list(bitonicSort(sample_input))
	# 	self.assertEqual(expected_output, res)
