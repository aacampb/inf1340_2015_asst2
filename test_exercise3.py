#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = 'Aaron Campbell, Sebastien Dagenais-Maniatopoulos & Susan Sim'
__email__ = "aaronl.campbell@mail.utoronto.ca, sebastien.maniatopoulos@mail.utoronto.ca & ses@drsusansim.org"
__copyright__ = "2015 Aaron Campbell & Sebastien Dagenais-Maniatopoulos & Susan Sim"
__license__ = "MIT License"

from exercise3 import schema_check, union, intersection, difference, MismatchedAttributesException

###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
			 [7274, "Robinson", 37],
			 [7432, "O'Malley", 39],
			 [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
			[9297, "O'Malley", 56],
			[7432, "O'Malley", 39],
			[9824, "Darkes", 38]]

# tables with mismatch headings in table1 and an extra column in table2

GRADS_WRONG = [["Number", "Surname", "Sex"],
			   [7274, "Robinson", "M"],
			   [7432, "O'Malley", "F"],
			   [9824, "Darkes", "N/A"]]

MNGRS_WRONG = [["Number", "Surname", "FirstName", "Sex"],
			   [9297, "O'Malley", "Martha", "F", ],
			   [7432, "O'Malley", "Clark" "M", ],
			   [9824, "Darkes", "Hortense", "F", ]]


#####################
# HELPER FUNCTIONS ##
#####################

def is_equal(t1, t2):
	return t1.sort() == t2.sort()


###################
# TEST FUNCTIONS ##
###################

def test_schema_check():
	"""
	Test to determine whether an error is thrown if the columns do not match
	"""
	try:
		schema_check(GRADUATES, MNGRS_WRONG)
	except MismatchedAttributesException:
		assert True
	else:
		assert False

	try:
		schema_check(GRADS_WRONG, MANAGERS)
	except MismatchedAttributesException:
		assert True
	else:
		assert False


def test_union():
	"""
    Test union operation.
    """

	result = [["Number", "Surname", "Age"],
			  [7274, "Robinson", 37],
			  [9297, "O'Malley", 56],
			  [7432, "O'Malley", 39],
			  [9824, "Darkes", 38]]

	assert is_equal(result, union(GRADUATES, MANAGERS))

	# test for MismatchedAttributesException

	try:
		union(GRADS_WRONG, MANAGERS)
	except MismatchedAttributesException:
		assert True
	else:
		assert False


def test_intersection():
	"""
    Test intersection operation.
    """
	result = [["Number", "Surname", "Age"],
			  [7432, "O'Malley", 39],
			  [9824, "Darkes", 38]]

	assert is_equal(result, intersection(GRADUATES, MANAGERS))

	# intersection mismatch

	try:
		intersection(GRADS_WRONG, MNGRS_WRONG)
	except MismatchedAttributesException:
		assert True
	else:
		assert False

	try:
		intersection(MANAGERS, GRADS_WRONG)
	except MismatchedAttributesException:
		assert True
	else:
		assert False


def test_difference():
	"""
    Test difference operation.
    """

	result = [["Number", "Surname", "Age"],
			  [7274, "Robinson", 37]]

	assert is_equal(result, difference(GRADUATES, MANAGERS))

	# mismatched tables

	try:
		difference(GRADS_WRONG, MANAGERS)
	except MismatchedAttributesException:
		assert True
	else:
		assert False

	try:
		difference(MNGRS_WRONG, MANAGERS)
	except MismatchedAttributesException:
		assert True
	else:
		assert False


LIBRARY_1 = [["Title", "Author_Last_Name", "Holdings"],
			 ["Hitcher's Guide to the Galaxy", "Adams", "Robarts"],
			 ["Suite Venitienne", "Calle", "Robarts"],
			 ["Practical Programming", "Gries, Campbell", "Robarts"],
			 ["Illuminations", "Benjamin", "Pratt"]]

LIBRARY_2 = [["Title", "Author_Last_Name", "Holdings"],
			 ["Hitcher's Guide to the Galaxy", "Adams", "Robarts"],
			 ["Restaurant at the End of the Universe", "Adams", "Pratt"],
			 ["Arcades Project", "Benjamin", "Robarts"],
			 ["Practical Programming", "Gries, Campbell", "Robarts"]]


def my_test_union():
	"""
    Test union operation.
    """
	result = [["Title", "Author_Last_Name", "Holdings"],
			  ["Hitcher's Guide to the Galaxy", "Adams", "Robarts"],
			  ["Suite Venitienne", "Calle", "Robarts"],
			  ["Practical Programming", "Gries, Campbell", "Robarts"],
			  ["Illuminations", "Benjamin", "Pratt"],
			  ["Restaurant at the End of the Universe", "Adams", "Pratt"],
			  ["Arcades Project", "Benjamin", "Robarts"]]

	assert result == union(LIBRARY_1, LIBRARY_2)


def my_test_intersection():
	"""
	Test intersection operation.
	"""
	result = [["Title", "Author_Last_Name", "Holdings"],
			  ["Hitcher's Guide to the Galaxy", "Adams", "Robarts"],
			  ["Practical Programming", "Gries, Campbell", "Robarts"]]

	assert result == intersection(LIBRARY_1, LIBRARY_2)


def my_test_difference():
	"""
	Test difference operation.
	"""
	result = [["Title", "Author_Last_Name", "Holdings"],
			  ["Suite Venitienne", "Calle", "Robarts"],
			  ["Illuminations", "Benjamin", "Pratt"]]

	assert result == difference(LIBRARY_1, LIBRARY_2)
