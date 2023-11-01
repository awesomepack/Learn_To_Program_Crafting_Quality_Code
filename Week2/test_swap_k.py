import unittest
from a1 import swap_k

class Test_swap(unittest.TestCase):

    ''' The test cases focus on the size of the input list, whether k is odd or even , and if the
    values in the list are negative or positve.'''
    def test_swap_k_given(self):

        '''The example given in a1 tests a list of average size | size'''

        self.assertEqual(swap_k([1,2,3,4,5, 6] , 2) ,[5,6,3,4,1,2] )

    def test_swap_k_empty(self):

        '''Testing with the special case where the list is empty | size'''

        self.assertEqual( swap_k([] , 0), [])

    def test_swap_k_negatives(self):

        '''Determining how the function deals with negative integers | Dichotomy'''

        self.assertEqual( swap_k([-1,2,3,-4] , 2) , [3,-4,-1,2])

    def test_swap_k_big_list(self):

        '''See how the function handles large lists | size'''
        self.assertEqual( swap_k([1,2,3,4,5,6,7,8,9,10,11] , 5) , [7,8,9,10,11,6,1,2,3,4,5])

    def test_swap_k_odd_list(self):

        '''Test against cases where the list is odd numbered | dichotomy'''

        self.assertEqual( swap_k([1,2,3] , 1) , [3,2,1])



if __name__ == '__main__':
    unittest.main()

    