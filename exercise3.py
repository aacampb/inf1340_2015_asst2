#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Aaron Campbell, Sebastien Dagenais-Maniatopoulos & Susan Sim'
__email__ = "aaronl.campbell@mail.utoronto.ca, sebastien.maniatopoulos@mail.utoronto.ca & ses@drsusansim.org"
__copyright__ = "2015 Aaron Campbell & Sebastien Dagenais-Maniatopoulos & Susan Sim"
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
    Function determines whether the schema of two tables contain matching attributes.

    :param table1: a table (a list of lists)
    :param table2: a table (a list of lists)
    :raise: MismatchedAttributesException:
            if table attributes do not match.
    """

    # compare the first row of each table
    if table1[0] != table2[0]:
        raise MismatchedAttributesException


def union(table1, table2):
    """
    Create a new table by combining one table with another.
    Remove duplicate table entries with remove_duplicates helper function.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
            if tables t1 and t2 don't have the same attributes
    """

    schema_check(table1, table2)
    table3 = table1 + table2
    return remove_duplicates(table3)


def intersection(table1, table2):
    """
    Create a new table containing all the unique rows from both tables.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
            if tables t1 and t2 don't have the same attributes
    """

    schema_check(table1, table2)
    intersection_list = []
    # iterate through rows in each table
    for lists1 in table1:
        for lists2 in table2:
            # compare the rows in each table to each other
            if lists1 == lists2:
                # add unique entries from second table to first table
                intersection_list.append(lists1)
    return intersection_list


def difference(table1, table2):
    """
    Create a new table that contains all of the unique rows from first table,
    but not the second table.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
            if tables t1 and t2 don't have the same attributes

    """

    schema_check(table1, table2)
    count = 1       # begin at index 1 to exclude table headers
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
