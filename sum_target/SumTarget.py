#!/usr/bin/env python
# vim: tabstop=8 expandtab widthsize=4 softtabstop=4

"""
Problem - A list of numbers is given. A target number (integer) is given. Write a function that returns a boolean value if any two numbers in list sum up the given target number.

Input -
List of integers
target integer

Output - 
True if any two integers in given list sum up given target integer
False if no two numbers in given list sum up given target integer

Assumption - 
1. No duplicate number is allowed in input list of integers
2. Each number can be used only once


"""

import logging
logging.basicConfig(level=logging.DEBUG)

def is_target_sum_achievable(input_list, target_integer): #take list of integers as arguments
    logging.debug("Input List: %s Target Integer: %s" %(input_list, target_integer))    
    len_input_list = len(input_list) #Capture length of input list

    #Edge case 01
    if len_input_list < 2: #Not a valid case
        logging.debug("Edge Case 01 - Input list container less than 2 items")    
        return False #Not possible

    #Edge case 02
    if len_input_list == 2: #Only two integers in list
        logging.debug("Edge Case 02 - Input list contains only two numbers")    
        if input_list[0] + input_list[1] == target_integer: #Sum of both elements equals to target integer
            logging.debug("Sum of both numbers %s and %s match the target: %s" %(input_list[0], input_list[1], target_integer))    
            return True
        else:
            logging.debug("Sum of both numbers %s and %s DON'T match the target: %s" %(input_list[0], input_list[1], target_integer))    
            return False

    #If length of input list is >=3 then proceed further
    members = set(input_list) #Form a set out of given list of integers to check membership

    logging.debug("Traversing provided input list")
    for item in input_list: #Traverse list
        logging.debug("Processing item: %s" %item)
        expected_value = target_integer - item #Expected value to meet sum criteria
        logging.debug("Checking if expected value %s is in the list: %s" %(expected_value, input_list))
        if expected_value != item and expected_value in members: #Assumption 2
            logging.debug("expected value found")
            logging.debug("Integer %s and Integer %s sum up %s" %(item, expected_value, target_integer))
            return True
            break #No need to proceed further
    else:
        logging.debug("No two integers found in the list: %s that sums up: %s" %(input_list, target_value))
        return False #else will execute only when for loop is exhausted


if __name__ == "__main__":
    raw_list = input("Enter space separated integers: ")
    input_list = []
    for item in raw_list.split():
        input_list.append(int(item))
    target_value = int(input("Enter target integer: "))
    output = is_target_sum_achievable(input_list, target_value)
    print(output)
