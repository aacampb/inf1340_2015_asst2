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
	Function to determine the index position of a of substring found within a string.
	:param input_string: string
	:param substring: string found in input_string
	:param start: beginning of input_string
	:param end: end of input_string
	:return:
	":raise: No exceptions will be raised
	"""
	count = 0
	position = start

	while position < end:
		if input_string[position] == substring[count]:
			count += 1
			if count == len(substring):
				return position - (len(substring)-1)
		else:
			count = 0
			# print position
		position += 1

	return -1

# find()


def multi_find(input_string, substring, start, end):
	"""
    Describe your function
    :param : we are essentially using the same formula as the our find function by using the find function
            in our tempResult function
     substring - What we are looking for in input_string
			 start - Start index for our search
			 end - End index for our search
			 count - tracks the amount of matching characters found in a row and keeps tracks of which character we are looking for
			 position - used as an indicator of which index we are currently at in our input_string

    :return: Function returns the starting index of the substring that has been located in the input_string.
    If the substring is not found: simply return -1
    If the substring is found, tempResult will continue until the next match is found until end.
    :raises: No exceptions will be raised
    """

    position = start
    result = ""

    while position < end-1:
        if result !="":
            result +=","



        tempResult = find(input_string, substring,position, end)
        position = tempResult + len(substring)
        result += str(tempResult)

    return result

# print multi_find("Ni!, Ni!, Ni!, Ni, Ni!", "Ni", 0, 20)
