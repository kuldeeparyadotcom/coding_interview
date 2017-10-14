#/usr/bin/python

"""
Purpose - To find top n frequent words from a given sample text file
"""

"""
Assumptions - 
1. Sufficient memory is available
2. Case insensitive word consideration
"""

import re
import sys
import logging
from collections import Counter

logging.basicConfig(level=logging.DEBUG)

def print_top_frequent_words(input_file, num): #Expects input text file and an integer
                                               #num - How many top frequent words to print
    pattern = re.compile(r'\w+')
    content = None #To hold file content
    try:
        with open(input_file, 'r') as f:
            content = f.read() #Whole content at once

    except FileNotFoundError:
        print("It seems provided file does not exist. Try again! Exiting...")
        sys.exit(1)

    words = re.findall(pattern, content) #Find all words in given content
    lower_words = [word.lower() for word in words]
    logging.debug(lower_words)

    most_common_words = Counter(lower_words).most_common(num)
    logging.debug(most_common_words)
    

if __name__ == "__main__":
    input_file = input("Enter file name to read: ") #i.e. ./sample_text
    num = int(input("How many top frequency words do you want to print out? : "))
    print_top_frequent_words(input_file, num) #Top 5 freuqncy words

