#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

"""
Purpose - Test BubbleSort program
"""

import unittest
import BubbleSort

class BubbleSortTestCase(unittest.TestCase):
    
    def test_edge_case_empty_input_list(self): #Exepcted to return input_list as it is
        self.assertTrue(BubbleSort.bubble_sort([]) == [])

    def test_edge_case_one_item_input_list(self): #Expected to return input_list as it is
        self.assertTrue(BubbleSort.bubble_sort([1]) == [1])

    def test_reversed_input_list(self):
        self.assertTrue(BubbleSort.bubble_sort([5, 4, 3, 2, 1]))

if __name__ == "__main__":
    unittest.main()
