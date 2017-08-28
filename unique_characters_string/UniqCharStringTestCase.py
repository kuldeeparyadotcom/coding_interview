#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

"""
    Purpose - To test Unique Character String functionality
"""

import unittest
import UniqCharStringSol1

class UniqCharStringTestCase(unittest.TestCase):
    
    #Edge Case - Empty string
    def test_empty_string(self):
        self.assertTrue(UniqCharStringSol1.is_unique_chars_string('') == '')

    #Edge Case - string of length 1
    def test_string_of_len_1(self):
        self.assertTrue(UniqCharStringSol1.is_unique_chars_string('a'))

    #Success case - 01
    def test_success_cases(self):
        input_set = ('abcde', 'abcdefg')
        for item in input_set:
            self.assertTrue(UniqCharStringSol1.is_unique_chars_string(item))

    #Failure case - 01
    def test_failure_cases(self):
        input_set = ('aabcde', 'goo')
        for item in input_set:
            self.assertFalse(UniqCharStringSol1.is_unique_chars_string(item))

if __name__ == "__main__":
    unittest.main()
