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
    :param : word - String will be tranformed into piglatin and returned as result.
				i - index indicator for string char position
    :return: returns a piglatin version of the initial "word" parameter as "result"
    :raises: No exceptions will be raised
	"""

	possibleVowels = "aeiouAEIOU"
	consonants = ""
	i = 0
	while i < len(word):
		if word[i] in possibleVowels: #is it a vowel?
			if i == 0: #If its the first itteration
				word = word + "yay" #add yay to the word
			break #stops the loop
		else:
			word = word[i:] + consonants + "ay"
			break #stops the loop
	else:
		consonants.append(word[i])

		i = i + 1

	result = word

	return result

# pig_latinify()

def pig_latinify(word):
	"""

	This function translates and English word into pig latin. Following the rules of pig latin,
	words that begin with vowels will be appended by "yay", and words that begin with a consonant
	will be appended by "ay".
	:param word: Takes a string as an input.
	:return: A modified string
	"""

	vowels = ["a", "e", "i", "o", "u"]
	word = str(word)
	word = word.lower()
	n = 0
	result = ""

	for letter in word:
		if word[n] in vowels:
			return word + "yay"
		else:
			n += 1
			if word[n] in vowels:
				return word[n:] +  word[:n] + "ay"
	return result

#pig_latinify()
