#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """

    result = ""

    n = 0
    word = word.lower()
    vowels = ["a", "e", "i", "o", "u"]
    if len(word) > 0 and word.isalpha() and not word.isdigit():
        for letter in word:
            first_letter = word[n]
            if first_letter in vowels:
                return word + "yay"
            else:
                n += 1
                letter = word[n]
                if letter in vowels:
                    return word[n:] + word[:n] + "ay"

    return result

#pig_latinify()
