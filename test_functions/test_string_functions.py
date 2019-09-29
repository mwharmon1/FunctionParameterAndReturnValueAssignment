"""
Author: Michael Harmon
Last Date Modified: 9/29/2019
Description: Unit tests to test the multiply_string
function in string_functions.py.
"""
import unittest
from more_functions import string_functions as sf


class MyTestCase(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(sf.multiply_string("Michael", 6), "MichaelMichaelMichaelMichaelMichaelMichael")


if __name__ == '__main__':
    unittest.main()
