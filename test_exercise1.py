#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = 'Aaron & Sebastien'
__github__ = "aacampb & 2015SebINF1340"
__copyright__ = "2015 Aaron & Sebastien"
__license__ = "MIT License"


from exercise1 import pig_latinify


def test_basic():
	"""
	Basic test cases from assignment hand out
	"""
	assert pig_latinify("dog") == "ogday"
	assert pig_latinify("scratch") == "atchscray"
	assert pig_latinify("is") == "isyay"
	assert pig_latinify("apple") == "appleyay"
	assert pig_latinify("scram") == "amscray"


def test_capitals():
	"""
	Test for words with capital letters
	"""
	assert pig_latinify("Aaron") == "aaronyay"
	assert pig_latinify("Toronto") == "orontotay"
	assert pig_latinify("pyThoN") == "onpythay"


def test_words_no_vowels():
	"""
	Test for words containing no vowels
	"""
	assert pig_latinify("cry") == "cryay"
	assert pig_latinify("sky") == "skyay"


def test_single_letter():
	"""
	Test words consisting of a single letter
	"""
	assert pig_latinify("a") == "ayay"
	assert pig_latinify("I") == "iyay"
