"""
Author: Michael Harmon
Last Date Modified: 9/29/2019
Description: This program will print a message based on values
entered by user.
"""


def multiply_string(message, n):
    """
    this function will accept 2 args and return a string message
    :param message: word to be multiplied by n
    :param n: amount of times message will display in single string
    :return: message multiplied by n in string
    """
    return message * int(n)


if __name__ == '__main__':
    multiply_string("Test", 4)
