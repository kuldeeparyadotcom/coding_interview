#!/usr/bin/env python

# vim: tabstop=8 tabspace shiftwidth=4 softtabstop=4

import unittest
import CompressString

class CompressStringTestCase(unittest.TestCase):
    def test_empty_input_string(self): #If input string is empty, don't process further and return empty string back
        self.assertTrue(CompressString.compress_string('') == '')

    def test_noncompliant_input_string(self):
        self.assertTrue(CompressString.compress_string('123') == '123')

    def test_input_string_AABBCC(self):
        self.assertTrue(CompressString.compress_string('AABBCC') == 'A2B2C2')

    def test_input_string_AAABCCDDDDD(self):
        self.assertTrue(CompressString.compress_string('AAABCCDDDDD') == 'A3B1C2D5')

    def test_input_string_abcABCAA(self):
        self.assertTrue(CompressString.compress_string('abcABCAA') == 'a1b1c1A1B1C1A2')

    def test_input_string_partial_pattern_match(self):
        self.assertTrue(CompressString.compress_string('aaaBBBbbb123') == 'aaaBBBbbb123')


if __name__ == "__main__":
    unittest.main()
