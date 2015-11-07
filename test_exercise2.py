#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing
Test module for exercise2.py
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from exercise2 import find, multi_find


def test_find_basic():
	"""
	Test find function.
	"""
	#tests whether our code actually works
	assert find("This is an ex-parrot", "parrot", 0, 20) == 14
	assert find("This is an ex-parrot", "Arthur", 0, 20) == -1
	assert find("I am Arthur, King of the Britons", "King", 0, 30) == 13
	assert find("I am Arthur, King of the Britons", "Who?", 0, 30) == -1


def test_multi_find_basic():
	"""
	Test multi_find function.
	"""
	#tests whether or not our code actually works
	assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"
	assert multi_find("Ni! Ni! NI! nI!", "ni", 0, 20) == "0,4,8,12"
	assert multi_find("Well, I didn't vote for you.", "Concord", 0, 30) == ""
