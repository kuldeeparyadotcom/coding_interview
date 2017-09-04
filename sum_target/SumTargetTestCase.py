#!/usr/bin/env python
# vim: tabstop=8 expandtab widthsize=4 softtabstop=4

import unittest
import SumTarget as st

class SumTargetTestCase(unittest.TestCase):
    
    def test_empty_input_list(self): #Edge Case 01
        self.assertFalse(st.is_target_sum_achievable([],2))

    def test_one_item_input_list(self): #Edge Case 02
        self.assertFalse(st.is_target_sum_achievable([1],2))

    def test_two_item_input_list(self): #Edge Case 02
        self.assertTrue(st.is_target_sum_achievable([1, 2],3))

    def test_random_item_input_list(self):
        self.assertTrue(st.is_target_sum_achievable([1, 5, 7, 9, 2, 3, 4], 16))

if __name__ == "__main__":
    unittest.main()


