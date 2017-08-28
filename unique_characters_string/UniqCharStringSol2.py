#!/usr/bin/env python

# vim: tabstop=8 expandtab widthsize=4 softtabstop=4

"""
    Purpose - To check if a given string is created by unique characters
    Input - A string i.e. ASCII and Unicode both supported
    Output - 
        True if string is made of unique characters
        False if string is not made of unique characters

"""

def is_unique_chars_string(input_string): #Method that takes a string input_string
    #Edge case 01 - Empty string
    if input_string == "": #check if input string is empty
        return input_string #return the input_string as it is

    length_of_input_string = len(input_string) #Capture lenght of input string for later use

    #Edge case 02 - Input string of length 1
    if length_of_input_string == 1: #Check if input string lengh is 1
        return True
    
    frequency_tracker = {} #Empty dictionary to track characters frequency

    for c in input_string: #Traverse input string
        if c in frequency_tracker: #Duplicate character
            return False
        else: #New character
            frequency_tracker[c] = 1

    return True #input_string consists of unique characters


if __name__ == "__main__":
    input_string = input("Enter a string to check if it is made of unique chars: ")
    print(is_unique_chars_string(input_string))
