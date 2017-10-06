#!/usr/bin/env python
# vim: tabstop=8 expandtab widthsize=4 softtabstop=4

class Node(object):
    
    """\
    Purpose - Simulate a tree Node
    """

    def __init__(self, val):
        self.l_child = None #Let child/subtree
        self.r_child = None #Right child/subtree
        self.data = val #Value of the node
    


def binary_insert(root, node): #Binary tree node insertion
    if root == None:
        root = node #Consider given node as root

    else:
        if root.data > node.data:
            if root.l_child == None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child == None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root): # in order traversal of given tree
    if not root:
        return
    in_order_print(root.l_child)
    print root.data
    in_order_print(root.r_child)

def pre_order_print(root): #pre order traversal
    if not root:
        return
    print root.data
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)

r = Node(3)
binary_insert(r, Node(7))
binary_insert(r, Node(1))
binary_insert(r, Node(5))


print "in-order"
in_order_print(r)

print "pre-order"
pre_order_print(r)
