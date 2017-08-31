#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

"""
Purpose - To implement bubble sort
Input - List of integers to be sorted out
Output - A sorted list
"""

import logging

logging.basicConfig(level=logging.CRITICAL)

def bubble_sort(input_list): #expects a list of integers

    len_input_list = len(input_list) #Capture length of input list

    #Edge case 01 - If input_list is empty
    if len_input_list < 1: #Empty list
        logging.debug("Edge case detected - empty list provided as input")
        return input_list #Return input_list as it is

    #Edge case 02 - If input_list is of length 1
    if len_input_list == 1: #Only one item - nothing to sort
        logging.debug("Edge case detected - one item list provided as input")
        return input_list #Return input_list as it is

    logging.debug("Starting sorting process..")
    for pass_num in range(len_input_list - 1): #Traverse each index except last
        logging.debug("Pass for index %s " %pass_num)
        for main_index in range(len_input_list - 1 ):
            next_index = main_index + 1 #next index marker
            current_item = input_list[main_index] #first item to compare
            next_item = input_list[next_index] #second adjacent item to compare with
            if current_item > next_item: #compare adjacent items
                logging.debug("Swap required as - item %s at index %s is > item %s at index %s" %(current_item, main_index, next_item, next_index))
                temp = current_item #swap in next three steps
                input_list[main_index] = next_item
                input_list[next_index] = temp
                logging.debug("Swapped %s with %s" %(current_item, next_item))
                logging.debug("After swap input_list looks like: %s" %input_list)
        logging.debug("After pass for index %s state of input_list: %s" %(pass_num, input_list))
    return input_list #Return input_list as it is mutable


if __name__ == "__main__":
    raw_data = input("Enter space separated numbers: ") 
    input_list = raw_data.split() #Bulid list out of user provided spaces separated int
    output = bubble_sort(input_list)
    print(output)

