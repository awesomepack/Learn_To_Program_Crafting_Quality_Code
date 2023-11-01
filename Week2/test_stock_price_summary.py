import unittest
from a1 import stock_price_summary

class Test_stock_price_summary(unittest.TestCase):

    '''Methods to test specific inputs to stock_price_summary() following all preconditions.
    Will mostly consider the size of the lists and whether values are positive or negative. Order
    does not matter much'''

    def test_stock_summary_a1(self):

        '''The example given in a1.py is a decent size and has a good mix of positive and
        negative values | Size
        '''
        self.assertEqual(stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01]) , (0.14,-0.17))

    def test_stock_summary_pos(self):

        ''' Testing output when the list is purely positive items | Dichotomy'''

        self.assertEqual(stock_price_summary([0.01 , 0.03 , 0.02 , 0.25]) , (0.31 , 0))

    def test_stock_summary_neg(self):

        ''' Testing output when the list is purely negative | Dichotomy'''

        self.assertEqual( stock_price_summary([-0.01 , -0.03 , -0.02 , -0.25]) , (0 , -.31))

    def test_stock_summary_empty(self):

        ''' Testing an empty list | Size'''

        self.assertEqual(stock_price_summary([]) , (0,0))



if __name__ == '__main__':
    unittest.main()

