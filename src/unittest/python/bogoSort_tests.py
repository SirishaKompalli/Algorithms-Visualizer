import unittest
from algorithms.bogoSort import bogoSort

class BogoSortTest(unittest.TestCase):
	def testCase1(self):
		sample_input = [13, 1]
		expected_output = [1, 13]
		res = list(bogoSort(sample_input))[0][0]
		self.assertEqual(expected_output, res)

	def testCase2(self):
		sample_input = []
		expected_output = []
		res = list(bogoSort(sample_input))
		self.assertEqual(expected_output, res)

	def testCase3(self):
		sample_input = [1, 2, 3, 4, 5]
		expected_output = [1, 2, 3, 4, 5]
		res = list(bogoSort(sample_input))[0][0]
		self.assertEqual(expected_output, res)

	def testCase4(self):
		sample_input = [13, 119, 456, 0, 12, 33]
		expected_output = [0, 12, 13, 33, 119, 456]
		res = list(bogoSort(sample_input))[0][0]
		self.assertEqual(expected_output, res)