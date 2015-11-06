#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def test_find_basic():
    """
    Test find function.
    """
    #tests whether our code actually works
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14

    #tests geared to generate errors based on the substring
    assert find("This is an ex-parrot", 1, 0, 20) == 14
    assert find("This is an ex-parrot", 3.3, 0, 20) == 14
    assert find("This is an ex-parrot", "PARROT", 0, 20) == 14
    assert find("This is an ex-parrot", "Parrot", 0, 20) == 14
    assert find("This is an ex-parrot", "arthur", 0, 20) == 14

    #tests geared to generate errors based on input_string
    assert find("This is an ex-general", "parrot", 0, 20) == 14
    assert find(10, "parrot", 0, 20) == 14
    assert find("10","parrot", 0, 20) == 14
    assert find("This is an ex-parot", "parrot", 0, 20) == 14
    assert find("3.5", "parrot", 0, 20) == 14
    

def test_multi_find_basic():
    """
    Test multi_find function.
    """
    #tests whether or not our code actually works
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"

    #tests geared to generate errors
    assert multi_find("Ni! Nay! Ni! Nay! Ni!", "Ni", 0, 20) == "0,4,8,12"
    assert multi_find(1, 2, 0, 20) == "0, 4, 8, 12"
    assert multi_find(2.0, 2, 0, 20) == "0,4,8, 12"

