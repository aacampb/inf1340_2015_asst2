

possibleVowels = "aeiouAEIOU"

def pig_latinify(word):
    """
    Describe your function
    :param : word - String will be tranformed into piglatin and returned as result.
	         i - index indicator for string char position
    :return: returns a piglatin version of the initial "word" parameter as "result"
    :raises: No exceptions will be raised
	"""
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
