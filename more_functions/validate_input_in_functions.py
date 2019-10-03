"""
Author: Michael Harmon
Last Date Modified: 10/02/2019
Description: This program will have a function that accepts args
and returns a string.
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
    validate input and return test name and test score in string
    :param test_name: name of test input by user
    :param test_score: default of 0 if not test score is input by user
    :param invalid_message: message to display when bad input ocurrs
    :return: test name: test score
    """
    if 0 < test_score <= 100:
        return test_name + ": " + str(test_score)
    else:
        return invalid_message

# pass


if __name__ == '__main__':
    score_input("Test")
