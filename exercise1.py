#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin
This module converts English words to Pig Latin words
"""

__author__ = 'Aaron Campbell, Sebastien Dagenais-Maniatopoulos & Susan Sim'
__email__ = "aaronl.campbell@mail.utoronto.ca, sebastien.maniatopoulos@mail.utoronto.ca & ses@drsusansim.org"
__copyright__ = "2015 Aaron Campbell & Sebastien Dagenais-Maniatopoulos & Susan Sim"
__license__ = "MIT License"


def pig_latinify(word):
	"""
	This function translates an English word into pig latin. Following the rules of pig latin,
	words that begin with vowels will be appended by "yay",
	and words that begin with a consonant will be appended by "ay".
	:param word: Takes a string as input.
	:return: A modified string.
	"""

	vowels = ["a", "e", "i", "o", "u"]
	word = word.lower()
	i = 0
	result = ""

	while i < len(word):
		if word[i] in vowels:		# not sure if this is needed?
			if i == 0:
				return word + "yay"
			break		# stops the loop
		else:
			try:
				i += 1
				if word[i] in vowels:
					return word[i:] + word[:i] + "ay"		# slice opening consonants & append to the end of word.
			except IndexError:		# to stop words without vowels crashing program (Thanks Graham!)
				return word + "ay"

	return result

# pig_latinify()
