import unittest
from algorithms.cocktailSort import cocktailSort

class CocktailSortTest(unittest.TestCase):
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

	def testCase3(self):
		sample_input = [1, 12, 34, 112]
		expected_output = [1, 12, 34, 112]
		res = list(cocktailSort(sample_input))[0][0]
		self.assertEqual(expected_output, res)

	def testCase4(self):
		sample_input = [1]
		expected_output = [1]
		res = list(cocktailSort(sample_input))[0][0]
		self.assertEqual(expected_output, res)

	def testCase4(self):
		sample_input = [5, 4, 3]
		expected_output = [3, 4, 5]
		res = list(cocktailSort(sample_input))[0][0]
		self.assertEqual(expected_output, res)

	def testCase5(self):
		sample_input = [5000000, 940001, 3000000]
		expected_output = [940001, 3000000, 5000000]
		res = list(cocktailSort(sample_input))[0][0]
		self.assertEqual(expected_output, res)



