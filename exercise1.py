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
	This function translates an English word into pig latin. Following the rules of pig latin,
	words that begin with vowels will be appended by "yay",
	and words that begin with a consonant will be appended by "ay".
	:param word: string will be translated into pig latin and returned as result.
	:return: returns a pig latin version of the initial "word" parameter as "result"
	"""

	vowels = ["a", "e", "i", "o", "u"]
	word = str(word)
	word = word.lower()
	i = 0
	result = ""

	while i < len(word):
		if word[i] in vowels:
			if i == 0:
				return word + "yay"
			break
		else:
			i += 1
			if word[i] in vowels:
				return word[i:] + word[:i] + "ay"
	return result

# pig_latinify()
