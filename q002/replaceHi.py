#!/bin/python
#Change the above line as per the target execution environment

"""
Purpose - To replace word "hi" occurrences with word "Hello"
Input - Command line argument - A valid text file (absolute path)
Output - In place expected occurrences replacement
  
"""

import sys
import re
import logging
import shutil #To backup input file before updating
from datetime import datetime #To capture timestamp in back up file naming convention

#Configure logger
logging.basicConfig(level=logging.DEBUG)

def usage(msg, code=1): #Default exit code 1 to refect incorrect usage
  print("Correct Usage: \n", sys.argv[0],"/path/to/input/file")
  print(msg)
  sys.exit(code)

#Input validation
def validate_input():
  if len(sys.argv) != 2:
    msg = "Requires absolute path of input file as command line argument\n You provided: " + str(len(sys.argv) - 1) + " arguments"
    usage(msg)


def replace_pattern(input_file, re_pattern, target_word):
  """
    Signature - replace_pattern(input_file, re_pattern, target_word, updated_content)
    Purpose - To replace a given pattern with a given string/word in a given file
    Input Arguments - 
      input_file - absolute path of the input file
      re_pattern - regex pattern to be replaced
      target_word - target word/string
    Output -
      returns a list of updated lines

  """
  updated_content=[] #To hold List of updated lines after designed pattern replacement
  with open(input_file,'r') as r: #Get a read only handler to the input file
    for line in r: #Traverse through each line in file
      logging.debug(line.split())
      if re_pattern.search(line): #Search for the target pattern "hi "
        updated_line = re.sub(re_pattern,target_word, line) #If pattern found and perform the sub
        updated_content.append(updated_line) #Append updated line to updated_content
      else:
        updated_content.append(line) #If match is not found, just preserve the original line
      logging.debug(updated_content)
  return updated_content

#Find and Replace pattern
validate_input()
re_pattern = re.compile(r"hi\s") #Pattern to be replaced
target_word = "Hello" #String to be replaced with
input_file=sys.argv[1] #Input file to operate on

#Call the method and get the udpated content
updated_content = replace_pattern(input_file, re_pattern, target_word)

#Open the input file in write mode and rewrite with updated content
timestamp = datetime.now().strftime("%y%m%d_%H%M%S") #Capture timestamp
backup_file = input_file + timestamp #Adopt a backup file naming convention
shutil.copyfile(input_file, backup_file) #Take backup before rewriting original file

with open(input_file,'w') as w: #Open input file in write mode
  for updated_line in updated_content: #Traverse through each line in udpated_content
    logging.debug("Writing line: %s" % updated_line)
    w.write(updated_line)
