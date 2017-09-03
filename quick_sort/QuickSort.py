#!/usr/bin/python
# vim: tabstop=8 expandtab widthsize=4 softtabstop=4

"""
Purpose - Quick Sort Implementation
Input -  A list of integers
Output - Sorted list
"""

import logging
logging.basicConfig(level=logging.DEBUG)

def quick_sort(input_list): #Function that takes a list i.e. input_list of numbers to be sorted

    #Capture some input characterstics that may be utilized in reaminer of program
    len_input_list = len(input_list)

    #Edge Case 01 - empty input_list
    if len_input_list < 1: #Empty input list
        logging.debug("Edge case 01 detected - empty input list - returning input list as it is")
        return input_list #Return input list as it is

    #Edge Case 02 - input list of size 1
    if len_input_list == 1: #input list of size 1
        logging.debug("Edge case 02 detected - input list of size 1 - returning input list as it is")
        return input_list #Return input list as it is, as it is considered to be already sorted
    
    #Process sorting list
    start = 0
    end = len_input_list - 1
    logging.debug("Calling helper function starting from index %s to all the way down to %s" % (start, end))
    quick_sort_helper(input_list, start, end) #recursive helper method


def quick_sort_helper(input_list, start, end):
    
    logging.debug("Processing %s from start: %s to end: %s" %(input_list, start, end))
    if start < end: #Recursion base case; Not a single element list
        logging.debug("As start: %s is less than end: %s hence proceeding.." % (start, end))
        split_point = partition(input_list, start, end)
        logging.debug("Got split point: %s" % split_point)

        logging.debug("Recursive call start on left half - list: %s start: %s end: %s" %(input_list, start, split_point -1 ))
        quick_sort_helper(input_list, start, split_point - 1 )

        logging.debug("Recursive call start on second half - list: %s start: %s end: %s" %(input_list, split_point + 1 , end))
        quick_sort_helper(input_list, split_point + 1, end)
        

def partition(input_list, start, end):

    logging.debug("Received call to partition list: %s start: %s end: %s" %(input_list, start, end))
    pivot_index = start
    pivot_value = input_list[pivot_index] #First value in list - Assumption for simplicity
    left_mark = start + 1
    right_mark = end

    done = False #Readability sake

    logging.debug("Starting pass")
    while not done:
        
        logging.debug("left_mark: %s right_mark: %s value at left mark: %s pivot_value: %s" %(left_mark, right_mark, input_list[left_mark], pivot_value))
        while (left_mark <= right_mark) and (input_list[left_mark] < pivot_value): #keep moving
            logging.debug("Left mark processing started")
            logging.debug("Moving left mark ahead.. as value at left mark: %s is less than pivot value: %s" %(input_list[left_mark], pivot_value))
            left_mark += 1 #Move right side; to the next index
            logging.debug("Left mark moved to index: %s" % left_mark)

        while (left_mark <= right_mark) and (input_list[right_mark] > pivot_value): #Keep moving
            logging.debug("Right mark processing started")
            logging.debug("Moving right mark to left as value at right mark: %s is greater than pivot value: %s" %(input_list[right_mark], pivot_value))
            right_mark -= 1 #Move left side; to the previous index
            logging.debug("Right Mark moved to index: %s" % right_mark)

        if (right_mark < left_mark): #mark crossed
            logging.debug("Marks crossed: right_mark: %s left_mark: %s" %(right_mark, left_mark))
            temp = input_list[right_mark] #swap pivot value with value at right_marker
            input_list[right_mark] = pivot_value
            input_list[pivot_index] = temp
            logging.debug("Items swapped: %s and %s" %(input_list[right_mark], pivot_value))

            done = True

        else: #If didn't cross yet
            #Swap value at left mark and right mark
           temp = input_list[right_mark]
           input_list[right_mark] = input_list[left_mark]
           input_list[left_mark] = temp

    return right_mark



if __name__ == "__main__":
    input_list = [1, 3, 4, 2]
    logging.debug("Input list to be sorted: %s" % input_list)
    quick_sort(input_list)
    logging.debug("Sorted list: %s" % input_list)

