#!/usr/bin/python

"""
Purpose - Simulate a linked list

TODO -
The following operations yet to be implemented ( Oct 14, 2017)
Search
Delete
"""

class Node(object): #simulate node of a linked list

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self): #Get value of a given node
        if self == None:
            return None
        else:
            return self.value

    def get_next_node(self): #Get next node reference
        if self == None:
            return None
        else:
            return self.next_node


class LinkedList(object): #Simulate a Liked List
    
    def __init__(self, root=None):
        if root == None:
            return None
        else:
            self.root = root

    def insert_node(self, root, node):
        if node == None:
                return self
        else:
            current_node = root #Given root
            if current_node.get_next_node() == None: #Only node
                current_node.next_node  = node #Attach the given node to it
            else:
                while (current_node.get_next_node() != None): #Find the last node
                    current_node = current_node.get_next_node()
                current_node.next_node = node #Attach given node at the end
                

    def display_linked_list(self, root):
        if root == None:
            return None
        else:
            current_node = root #Given root
            
            while (current_node.get_next_node() != None): #Print remaining nodes
                print(current_node.get_value())
                current_node = current_node.get_next_node()
            print(current_node.get_value()) #Print last node

    def get_all_node_values(self, root):
        node_values_list = [] #List to hold values of all nodes
        if root == None:
            return None
        else:
            current_node = root #Given root
            
            while (current_node.get_next_node() != None): #Print remaining nodes
                node_values_list.append(current_node.get_value())
                current_node = current_node.get_next_node()
            node_values_list.append(current_node.get_value()) #Print last node
            return node_values_list

    def len_linked_list(self, root):
        counter = None
        if root == None:
            return None
        else:
            counter = 1 #Start counter initialized with 1 (as at least root node found)
            current_node = root #Given root
            
            while (current_node.get_next_node() != None): #Count remaining nodes
                counter += 1 #Increment counter by 1
                current_node = current_node.get_next_node()
        return counter

if __name__ == "__main__":
    #Try to build a linked list
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #input list to build linked list from
    root = None
    ll = None
    for ind, item in enumerate(input_list): #Enumerate over given list
        if ind == 0: #Treat first item of the list as root of the linked list
            root = Node(item) #Build root Node from first element
        else:
            node = Node(item)
            ll = LinkedList(root) #Make Linked List starting from root node
            ll.insert_node(root, node) #Keep inserting nodes
    
    print("Length of linked list: ", ll.len_linked_list(root))
    print("Linked List items - ")
    ll.display_linked_list(root)
