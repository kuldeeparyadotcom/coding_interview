#!/usr/local/bin/python
#vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

"""
Purpose - Unit test cases for the program get_string_permutations.py
"""

import unittest
import math
import get_string_permutations as gsp

class Test_Get_String_Permutations(unittest.TestCase): #Base class of unittest.TestCase

    def test_empty_string(self): #Edge case
        self.assertTrue(gsp.get_permutations('') == set()) #Expected result is empty set

    def test_two_chars_string(self): #String of two unique characters
        self.assertTrue(gsp.get_permutations('ab') == {'ab', 'ba'})

    def test_three_chars_string(self): #String of three unique chatacters
        self.assertTrue(gsp.get_permutations('abc') == {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'})
    
    def test_seven_chars_string(self): #String of seven characters - interested in count only
        self.assertTrue(math.factorial(7) == len(gsp.get_permutations('abcdefg'))) #number of permutations factorial of 7

if __name__ == "__main__":
    unittest.main()
