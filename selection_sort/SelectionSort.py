#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

"""
    Purpose - To implement selection sort
        Input - List of integers to be sorted out
        Output - A sorted list
"""

import logging

logging.basicConfig(level=logging.CRITICAL)

def selection_sort(input_list): #expects a list of integers

    len_input_list = len(input_list) #Capture length of input list

    #Edge case 01 - If input_list is empty
    if len_input_list < 1: #Empty list
        logging.debug("Edge case detected - empty list provided as input")
        return input_list #Return input_list as it is

    #Edge case 02 - If input_list is of length 1
    if len_input_list == 1: #Only one item - nothing to sort
        logging.debug("Edge case detected - one item list provided as input")
        return input_list #Return input_list as it is

    for end_index_for_current_pass in range(len_input_list - 1, 0, -1): #Traverse only till required index in each pass
        largest_currently_at_index = end_index_for_current_pass #Assume largest number is at right place

        for current_index in range(0, end_index_for_current_pass): #Traverse from index 0 to the required end index for pass
            next_index = current_index + 1
            
            #Compare adjacent items and just keep track of the index of largest number
            if input_list[current_index] > input_list[largest_currently_at_index]:
                largest_currently_at_index = current_index

        if end_index_for_current_pass != largest_currently_at_index: #If largest number is not alreay in place
            logging.debug("As largest number is not in place, hence initiating swapping..")
            logging.debug("Currently largest number %s is at index %s but it should be at index %s" %(input_list[largest_currently_at_index], largest_currently_at_index, end_index_for_current_pass))
            temp = input_list[end_index_for_current_pass]
            input_list[end_index_for_current_pass] = input_list[largest_currently_at_index] #Swap if required
            input_list[largest_currently_at_index] = temp
            logging.debug("Swap complete, items %s and %s are swapped" %(input_list[end_index_for_current_pass], input_list[largest_currently_at_index]))
            logging.debug("After swap input_list looks like: %s" %input_list)


        logging.debug("Pass %s completed!" %(len_input_list - end_index_for_current_pass))
        logging.debug("Current state of input_list: %s" %input_list)

    return input_list #Return input_list as it is mutable


if __name__ == "__main__":
    raw_data = input("Enter space separated numbers: ") 
    input_list = raw_data.split() #Bulid list out of user provided spaces separated int
    output = selection_sort(input_list)
    print(output)

