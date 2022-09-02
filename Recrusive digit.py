
"""We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.

If  has only  digit, then its super digit is .
Otherwise, the super digit of  is equal to the super digit of the sum of the digits of
super_digit(9875)   	9+8+7+5 = 29
	super_digit(29) 	2 + 9 = 11
	super_digit(11)		1 + 1 = 2
	super_digit(2)		= 2 ."""
import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
