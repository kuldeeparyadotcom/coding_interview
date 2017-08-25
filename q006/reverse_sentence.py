#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import logging
logging.basicConfig(level=logging.DEBUG)

def reverse_sentence(sen):
    """
        Purpose - reverse a given sentence
            For example - "this is awesome" becomes "awesome is this"
        Input - sentence
        Output - returns reversed sentence
    """
    logging.debug("Removing leading and training spaces of: %s" %sen)
    s = sen.strip() #Get rid of leading and trailing spaces
    logging.debug("After removal of spaces: %s" %s)

    logging.debug("Splitting given sentence: %s" %s)
    list_of_words = s.split()
    logging.debug("After split: %s" % list_of_words)

    logging.debug("Reversing splitted sentence")
    list_of_words.reverse()
    logging.debug("Reversed list of words: %s" % list_of_words)

    reversed_sentence = " ".join(list_of_words)

    return reversed_sentence
    
            
if __name__ == "__main__":
    sen = input("Enter a sentence to reverse: ")
    result = reverse_sentence(sen)
    print(result)
