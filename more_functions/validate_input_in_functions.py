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
    :param test_score: default of 0 if no test score is input by user
    :param invalid_message: message to display when bad input occurs
    :return: test name: test score
    """
    try:
        test_score = int(test_score)
    except ValueError:
        return invalid_message

    if test_score < 0 or test_score > 100:
        return invalid_message
    else:
        return test_name + ": " + str(test_score)


if __name__ == '__main__':
    print(score_input('TestName', 88))
