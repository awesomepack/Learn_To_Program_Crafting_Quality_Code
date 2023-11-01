import unittest
from a1 import num_buses

class test_num_buses(unittest.TestCase):

    '''The tests mostly focus on the size of n and whether it is at a threshold
    Because of the precondtion negative values are of no concern.'''

    def test_num_buses_a1(self):

        '''The test case given in a1 is a good way to test what happens when
        n is not evenly divided by 50'''

        self.assertEqual( num_buses(75) , 2)

    def test_num_buses_0(self):
        
        '''Testing the function at the threshold of the precondition, 0 | Threshold'''

        self.assertEqual( num_buses(0) , 0)

    def test_num_buses_large(self):

        '''Testing the function at a very large number | Size'''

        self.assertEqual( num_buses(999999999) , 20000000)

    def test_num_buses_50(self):

        '''Testing the function at the max capacity of 1 bus | Threshold'''
        self.assertEqual( num_buses(50) , 1)



if __name__ == '__main__':
    unittest.main()