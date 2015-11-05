#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    A function to find the index value of the start of a substring
    contained within a longer string.

    :param : input_string, substring, start, end
    :return: index value of first letter of substring
    :raises: return -1 if substring not found

    """
    # find substring in input_string
    # iterate through input_string until substring found
    # if substring found return index of substring
    # if substring not found return -1

    input_string = input_string.lower()
    substring = substring.lower()
    index = 0

    if substring in input_string:
        index = input_string.index(substring, start, end)
        return index
    return -1

# find()

# test cases:
# ("This is an ex-parrot", "parrot", 0, 20) returned 14
# ("This is an ex-parrot", "Ni!", 0, 20) returned -1
# ("Yes, hear Joyce say 'Yes' in Ulysses.", "yes", 0, 40), returned 0
# ("Yes, hear Joyce say 'Yes' in Ulysses.", "say", 0, 40), returned 16
# ("Yes, hear Joyce say 'Yes' in Ulysses.", "Parrot", 0, 40), returned -1

def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""

    return result
