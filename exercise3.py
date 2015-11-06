#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


GRADUATES = [["Number", "Surname", "Age"],
            [7274, "Robinson", 37],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]

def schema_check(table1, table2):
    """

    :return:
    """
    # determine whether the 2 tables contain identical attributes: Number, Surname, Age
    # return a new table that contains all unique rows that appear in either table

    if table1[0] != table2[0]:
        raise MismatchedAttributesException

def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    schema_check(table1, table2)        #put at the beginning of each function

    table3 = table1 + table2
    return remove_duplicates(table3)

def intersection(table1, table2):
    """
    Describe your function

    """
    # return a new table with all unique rows from both tables

    schema_check(table1, table2)

    intersection_list = []
    for lists1 in table1:
        for lists2 in table2:
            if lists1 == lists2:
                intersection_list.append(lists1)
    return intersection_list


def difference(table1, table2):
    """
    Describe your function

    """
    schema_check(table1, table2)

    count = 1

    while count < len(table1):
        for lists2 in table2:
            if table1[count] == lists2:
                table1.remove(table1[count])
        count += 1
    return table1


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass
