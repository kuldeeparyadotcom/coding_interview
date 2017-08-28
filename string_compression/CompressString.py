#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=8

"""
Purpose: Compress given string
Expected Input - A string containing only [a-z][A-Z]
Optput - compressed string (False compression allowed)
"""

import logging
import re

#configure logger
logging.basicConfig(level=logging.CRITICAL)

re_exp = re.compile("[a-z]*[A-Z]*")

def compress_string(input_string): #method to compress string; requires only a string
    logging.debug("Input String: %s" %input_string)

    #Edge Case 01 - Empty String
    if len(input_string) < 1: #Edge Case for string of length 0
        logging.debug("Input String length: %s" %len(input_string))
        return input_string

    mo = re_exp.search(input_string) #Cofirm if given string is compliant to the expected pattern
    logging.debug("Match object group: %s" % mo.group())

    match = mo.group()

    #Edge Case 02 - No Match
    if not match: #If string match does not compliant with expected pattern
        logging.debug("Input string does not match with expected pattern")
        return input_string

    #Edge Case 03 - Partial Match
    if match: #considering match is there
        if len(str(match)) != len(input_string): #If full match is not there
            logging.debug("It seems a partial match case. Only the following part matches with expected pattern %s" % match)
            return input_string

    #Compression process
    frequency_tracker = {} #Empty string to track letter frequency
    sequence_tracker = [] #List to track chatacters sequence in string as Dict will not maintain order
    compressed_string = [] #To hold compressed string
    
    for item in input_string: #Traverse through string
        logging.debug("Processing character: %s" % item)
        if item in frequency_tracker: #if t already exists in dictionary
            last_seen_character = sequence_tracker[-1]
            logging.debug("Last seen character: %s" %last_seen_character)
            if last_seen_character == item: #Increment frequency only if last seen character is same
                logging.debug("Incrementing frequency of character: %s" % item)
                frequency_tracker[item] += 1 #increment frequency by one
                compressed_string[-1] = str(frequency_tracker[item])
            else:
                logging.debug("Current character is not in continuation")
                logging.debug("Resetting frequency of %s to 1 " %item)
                frequency_tracker[item] = 1 #Reset frequency to 1 as chacters not in sequence
                compressed_string.append(item)
                compressed_string.append(str(frequency_tracker[item]))
                sequence_tracker.append(item) #To capture order

        else: #If a new key for dictionary
            logging.debug("Initilizing frequency for character: %s" % item)
            sequence_tracker.append(item) #To capture order
            frequency_tracker[item] = 1 #Intialize value by 1

            compressed_string.append(item)
            compressed_string.append(str(frequency_tracker[item]))
        logging.debug("current state of compresses string list: %s" %compressed_string)

    logging.debug("Current state of frequency tracker: %s" %frequency_tracker)

    #Form compressed string
    #for i in sequence_tracker: #Traverse sequence tracker
    #    compressed_string.append(i) #Append character
    #    compressed_string.append(str(frequency_tracker[i])) #Append respective captured frequency
    return "".join(compressed_string)


if __name__ == "__main__":
    input_string = input("Enter some string [a-zA-Z] to get compressed: ")
    compressed_string = compress_string(input_string.strip())
    print("Compresssed String: %s" % compressed_string)
