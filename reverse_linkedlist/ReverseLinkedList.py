#!/usr/bin/env python
# vim: tabstop=8 expandtab widthsize=4 softtabstop=4

""" \
Purpose - Implement a singly linked list and demonstrate reversal.
"""

import logging
logging.basicConfig(level=logging.DEBUG)

class Node(object): #Node simulation
  
    def __init__(self, data, next_node = None): #Node simulation
        logging.debug("Manufacturing new node.." )
        self.next_node = next_node #pointer to next node
        logging.debug("Node's next node: %s" %self.next_node)
        self.data = data #value of the node
        logging.debug("Node's data: %s" %self.data)

    def get_data(self):
        return self.data #Return value

    def get_next(self):
        return self.next_node #Return pointer to next node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data) #Create new node
        new_node.set_next(self.head) #push current head down the line
        self.head = new_node #New node becomes the new head

    def print_linked_list(self):
        logging.debug("self head: %s" %self.head)
        if self.head == None: #Empty list
            return
        else:
            while not self.head == None:
                print(self.head.get_data())
                self.head = self.head.get_next()

    def reverse_linked_list(self):
        logging.debug("Reversing given linked list..")
        temp_stack = [] #Stack for reversal
        if self == None: #Empty linked list
            logging.debug("Empty linked list passed")
            return
        else:
            logging.debug("self.head %s" %self.head)
            while not self.head == None:
                temp_stack.append(self.head)
                print("Pushing %s to temp stack" % self.head.get_data())
                self.head = self.head.get_next()
        




if __name__ == "__main__":
    ll = LinkedList()
    ll.print_linked_list()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)

    ll.print_linked_list()

    ll.reverse_linked_list()
