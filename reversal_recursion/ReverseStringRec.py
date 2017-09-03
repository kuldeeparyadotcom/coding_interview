#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

"""
Purpose - To demonstrate string reversal using recursion
"""

import logging
logging.basicConfig(level=logging.DEBUG)

def reverse_rec(input_string): #Function that takes a string as input and reverses string

    #Edge case 01 - Empty string or one character string
    if len(input_string) < 2:
        return input_string

    input_list = list(input_string) #Form a list to utilize python list methods
    
    reversed_string = [] #Empty list to hold reversed string
    logging.debug("Reversed string: %s" % reversed_string)
    reverse_rec_helper(input_list, reversed_string)
    return ''.join(reversed_string)

def reverse_rec_helper(input_list, reversed_string): #Rec helper method
    logging.debug("length of input_list: %s", len(input_list))
    if len(input_list) >= 1: #Recursion base case - empty input_list

        last_char = input_list[-1] #Take last character out
        reversed_string.append(last_char) #Append it to temporary storage - list
        input_list.pop() #Delete the last element from input_list
        reverse_rec_helper(input_list, reversed_string) #Recursion call

if __name__ == "__main__":
    input_string = input("Enter a string to reverse: ")
    print(reverse_rec(input_string.strip()))
