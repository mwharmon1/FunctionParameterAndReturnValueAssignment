import unittest
from more_functions import validate_input_in_functions as v


class MyTestCase(unittest.TestCase):
    # mandatory arg test
    def test_score_input_test_name(self):
        self.assertEqual(v.score_input("MathTest"), 'MathTest: 0')

    # mandatory arg and optional test_score arg tests
    def test_score_input_test_score_valid(self):
        self.assertEqual(v.score_input("Unit4", test_score=80), 'Unit4: 80')

    def test_score_input_test_score_below_range(self):
        self.assertEqual(v.score_input("Unit1", test_score=-10), 'Invalid test score, try again!')

    def test_score_input_test_score_above_range(self):
        self.assertEqual(v.score_input("PythonTest", test_score=112), 'Invalid test score, try again!')

    def test_test_score_non_numeric(self):
        self.assertEqual(v.score_input("Unit5", 'NonNumeric'), 'Invalid test score, try again!')

    # all args test
    def test_score_input_invalid_message(self):
        self.assertEqual(v.score_input("ScienceTest", test_score=101), 'Invalid test score, try again!')


if __name__ == '__main__':
    unittest.main()
