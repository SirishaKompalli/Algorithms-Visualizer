import unittest

from algorithms.pancakeSort import pancakeSort


class PancakeSortTest(unittest.TestCase):
    #testCasel - unsorted array 
    def testCasel(self):
        inputArray = [3, 67, 4, 1, 8, 0, 54, 78]
        expectedOutputArray = [0, 1, 3, 4, 8, 54, 67, 78]
        #print ("Input: ", input_array)
        OutputArray = list(pancakeSort(inputArray))[0][0]
        #print ("Output: ", array)
        self.assertEqual(expectedOutputArray, OutputArray)

    #testCase2 - empty array     
    def testCase2(self):
        inputArray = []
        expectedOutputArray = []
        #print ("Input: ", input_array)
        OutputArray = list(pancakeSort(inputArray))
        #print ("Output: ", array)
        self.assertEqual(expectedOutputArray, OutputArray)

    #testCase3 - negative integer array
    def testCase3(self):
        inputArray = [-3, -67, -4, -1, -8, 0, -54, -78]
        expectedOutputArray = [-78, -67, -54, -8, -4, -3, -1, 0]
        #print ("Expected Output: ", expectedOutputArray)
        OutputArray = list(pancakeSort(inputArray))[0][0]
        #print ("Output: ", OutputArray)
        self.assertEqual(expectedOutputArray, OutputArray)

    #testCase4 - floating number array   
    def testCase4(self):
        inputArray = [3.5, 67.1, 4, 0.1, 8, 0.2, 54, 78]
        expectedOutputArray = [0.1, 0.2, 3.5, 4, 8, 54, 67.1, 78]
        #print ("Input: ", expectedOutputArray)
        OutputArray = list(pancakeSort(inputArray))[0][0]
        #print ("Output: ", OutputArray)
        self.assertEqual(expectedOutputArray, OutputArray)

    #testCase5 - sorted array
    def testCase5(self):
        inputArray = [0, 1, 3, 4, 8, 54, 67, 78]
        expectedOutputArray = [0, 1, 3, 4, 8, 54, 67, 78]
        #print ("Input: ", expectedOutputArray)
        #input array is modified by pancakeSort
        list(pancakeSort(inputArray))
        #print ("Output: ", inputArray)
        self.assertEqual(expectedOutputArray, inputArray)
    
    #testCase6 - same value array     
    def testCase6(self):
        inputArray = [3, 3, 3, 3]
        expectedOutputArray = [3, 3, 3, 3]
        #print ("Input: ", expectedOutputArray)
        #input array is modified by pancakeSort
        list(pancakeSort(inputArray))
        #print ("Output: ", inputArray)
        self.assertEqual(expectedOutputArray, inputArray)        