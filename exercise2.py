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
Describe your function
    :param : input_string - String in which the substring must be located
	substring - What we are looking for in input_string
	start - Start index for our search
	end - End index for our search
	count - tracks the ammount of matching characters found in a row and keeps tracks of which character we are looking for
	position - used as an indicator of which index we are currently at in our input_string

    :return: Function returns the starting index of the substring that has been located in the input_string. If the substring is not found: simply return -1
    :raises: No exceptions will be raised
    """
count = 0
position = start

while position < end:
    if input_string[position] == substring[count]:
	count += 1
	if count == len(substring):
	    return position - len(substring)
    else:
  	count = 0;

	position +=1

    return -1


def multi_find(input_string, substring, start, end):
    """
    Describe your function
    :param :
    :return:
    :raises:
    """

position = start
result = ""

while position < end:
    tempResult = find(input_string, substring,position, end)
position = tempResult + len(substring)
result += tempResult + ","

return result

