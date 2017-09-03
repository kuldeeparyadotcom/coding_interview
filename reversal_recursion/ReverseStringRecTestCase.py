#!/usr/bin/env python
# vim: tabstop=8 expandtab widthsize=4 softtabstop=4

"""
Purpose - To test ReverseStringRec.py
"""

import unittest
import ReverseStringRec as rsr

class ReverseStringRecTestCase(unittest.TestCase):

    def test_edge_empty_string(self): #Edge case - empty string
        self.assertTrue(rsr.reverse_rec('') == '')


    def test_random_string(self):
        self.assertTrue(rsr.reverse_rec('abcdef') == 'fedcba')


if __name__ == "__main__":
    unittest.main()
