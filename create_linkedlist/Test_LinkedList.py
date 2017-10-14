#/usr/bin/python

"""
Purpose - Test LinkedList.py
"""

import unittest
import LinkedList as myll
from LinkedList import Node

#Prepare some test data - Try to build a linked list
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #input list to build linked list from
root = None
ll = None
for ind, item in enumerate(input_list): #Enumerate over given list
    if ind == 0: #Treat first item of the list as root of the linked list
        root = Node(item) #Build root Node from first element
    else:
        node = Node(item)
        ll = myll.LinkedList(root) #Make Linked List starting from root node
        ll.insert_node(root, node) #Keep inserting nodes
  
#print(ll.len_linked_list(root))
#ll.display_linked_list(root)
#print(ll.get_all_node_values(root))

class Test_LinkedList(unittest.TestCase):

    def test_happy_scenario_length_check_01(self):
        self.assertTrue(ll.len_linked_list(root)==10)

    def test_happy_scenario_values_check_01(self):
        self.assertTrue(ll.get_all_node_values(root)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == "__main__":
    unittest.main()
