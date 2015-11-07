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
	Function to find a substring within a longer string.
	:param :
	:return : index value of the first character of substring found in input_string
	:raises :
	"""


	index = 0
	input_string = input_string.lower()
	substring = substring.lower()
	for ch in range(start, end):
		if input_string[index:index + len(substring)] == substring:
			return index
		index += 1
	else:
		return -1

# print find("I am Arthur, King of the Britons", "King", 0, 30)


def multi_find(input_string, substring, start, end):
	"""

	:param input_string:
	:param substring:
	:param start:
	:param end:
	:return:
	"""

	index = 0
	input_string = input_string.lower()
	substring = substring.lower()
	result = ""
	while index < end:
		for ch in range(start, end):
			if input_string[index:index + len(substring)] == substring:
				result += str(index) + ","
			index += 1
		result = result[0:-1]
		return result
	else:
		return ""

# print multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20)
