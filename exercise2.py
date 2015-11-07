#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing
This module converts performs substring matching for DNA sequencing
"""

__author__ = 'Aaron Campbell, Sebastien Dagenais-Maniatopoulos & Susan Sim'
__email__ = "aaronl.campbell@mail.utoronto.ca, sebastien.maniatopoulos@mail.utoronto.ca & ses@drsusansim.org"
__copyright__ = "2015 Aaron Campbell & Sebastien Dagenais-Maniatopoulos & Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
	"""
	Function to find a substring within a longer string.
	:param input_string: phrase or string of letters
	:param substring: string found within input_string
	:param start: first index position of input_string
	:param end: last index position of input_string
	:return : index value of the first character of substring found in input_string
	:raises :
	"""

	index = 0
	input_string = input_string.lower()		# correct for variations in case
	substring = substring.lower()
	for ch in range(start, end):		# iterate through the string
		if input_string[index:index + len(substring)] == substring:		# compare slice from both strings
			return index
		index += 1
	else:
		return -1

# find()


def multi_find(input_string, substring, start, end):
	"""
	Function to find all of the instances of a substring within in a longer string.
	Return a list of the index value for the first character of each found instance.

	:param input_string: phrase or string of letters
	:param substring: string found within input_string
	:param start: first index position of input_string
	:param end: last index position of input_string
	:return: list of index values of first character of each instance of substring found in input_string,
			returns empty string if no instances found
	"""

	index = 0
	input_string = input_string.lower()
	substring = substring.lower()
	result = ""
	while index < end:
		for ch in range(start, end):
			if input_string[index:index + len(substring)] == substring:
				result += str(index) + ","		# convert int
			index += 1
		result = result[0:-1]		# return slice of all index points
		return result
	else:
		return ""

# multi_find()
