#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import logging
logging.basicConfig(level=logging.DEBUG)

def is_anagram(str1, str2):
    """
        Purpose: To check if provided two strings are anagram or not
        Constraints - case insensitive, spaces ignored
        Input - 
            str1 - first string
            str2 - second string
        Output - 
            returns 
                True - if provided strings are anagrams
                False - if provided strings are not anagrams
    """
    logging.debug("Lowercase first string")
    first = str1.lower() #Lowercase first string
    logging.debug("Lowered case to: %s" % first)

    logging.debug("Lowercase second string")
    second = str2.lower() #lowercase second string
    logging.debug("Lowered case to: %s" % second)

    #Litmus test
    #Provided strings are not anagrams if number of charactes in both are different
    if len(set(first)) != len(set(second)):
        return False
    

    #Use data strucutre List as single place to compare
    anagram_checker = [True]*128 #Empty list with default references to True

    logging.debug("Traversing first string: %s" %first)
    for c in first: #Traverse every character in first string
        logging.debug("Processing character %s" %c)
        if c == ' ': #Ignore spaces
            continue
        anagram_checker[ord(c)] = False #For each character c, set corresponding reference to False at index ord(c)
    logging.debug("First string traversal completed: %s" %str(anagram_checker))


    #Traverse second string
    logging.debug("Traversing second string: %s" %second)
    for c in second: #Traverse every character in second string
        logging.debug("Processing character %s" %c)
        if c == ' ': #Ignore spaces
            continue
        anagram_checker[ord(c)] = True #For each character c, set corresponding reference to True at index ord(c)
    logging.debug("First string traversal completed: %s" %str(anagram_checker))


    #Check list anagram_checker
    for item in anagram_checker: #Traverse anagram_checker list
        if not item: #If any item is found to be False that means provided strings are not anagrams
            return False
    else:
        return True


if __name__ == "__main__":
    first = input("Enter first string: ")
    second = input("Enter second string: ")
    if is_anagram(first, second):
        print("Anagrms")
    else:
        print("Not Anagrams")
