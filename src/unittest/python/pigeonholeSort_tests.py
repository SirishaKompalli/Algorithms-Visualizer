import unittest

from algorithms.pigeonholeSort import pigeonholeSort


class PigeonholeSortTest(unittest.TestCase):
    #testCasel - unsorted array 
    def testCasel(self):
        inputArray = [3, 67, 4, 1, 8, 0, 54, 78]
        expectedOutputArray = [0, 1, 3, 4, 8, 54, 67, 78]
        #print ("Input: ", input_array)
        OutputArray = list(pigeonholeSort(inputArray))[0][0]
        #print ("Output: ", array)
        self.assertEqual(expectedOutputArray, OutputArray)

    #testCase2 - negative integer array
    def testCase2(self):
        inputArray = [-3, -67, -4, -1, -8, 0, -54, -78]
        expectedOutputArray = [-78, -67, -54, -8, -4, -3, -1, 0]
        #print ("Expected Output: ", expectedOutputArray)
        OutputArray = list(pigeonholeSort(inputArray))[0][0]
        #print ("Output: ", OutputArray)
        self.assertEqual(expectedOutputArray, OutputArray)

    #testCase3 - sorted array
    def testCase3(self):
        inputArray = [0, 1, 3, 4, 8, 54, 67, 78]
        expectedOutputArray = [0, 1, 3, 4, 8, 54, 67, 78]
        #print ("Input: ", expectedOutputArray)
        #input array is modified by pigeonholeSort
        list(pigeonholeSort(inputArray))
        #print ("Output: ", inputArray)
        self.assertEqual(expectedOutputArray, inputArray)
    
    #testCase4 - same value array     
    def testCase4(self):
        inputArray = [3, 3, 3, 3]
        expectedOutputArray = [3, 3, 3, 3]
        #print ("Input: ", expectedOutputArray)
        #input array is modified by pigeonholeSort
        list(pigeonholeSort(inputArray))
        #print ("Output: ", inputArray)
        self.assertEqual(expectedOutputArray, inputArray)        