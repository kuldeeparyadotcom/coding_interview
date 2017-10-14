#/usr/bin/python

"""
Purpose - To find top n frequent words from a given sample text file
"""

def build_dict_of_words(input_file): #Expects a file as input
    try:
        seen_words = set() #A set to hold the words (It can be avoided if using python collections as collections dict doesn't throw error if key does not exist)
        frequency_tracker = {} #Empty dictionary to track words frequency

        with open(input_file, 'r') as f:
            for line in f: #read each line one by one
                words = line.lower().split() #Assumption 01 - words are separated by space - default separator
                                         #Assumption 02 - Case insensitive appraoch
                for word in words:
                    if word in seen_words: #Check membership using a set before attempting to access dictionary with this word as key (to avoid key error if tired to directly access dict with this key)
                        frequency_tracker[word] += 1 #Increment frequency of seen word by 1
                    else:
                        seen_words.add(word) #Add words to set of seen_words
                        frequency_tracker[word] = 1 #Initialize frequency by one for the first time for the word
    except FileNotFoundError: #If input_file does not exist
        print("It seems provided file to read does not exist. Exiting...")
    return frequency_tracker
        
def build_list_of_tuples_from_dict(input_dict): #Expects an dicationary as input
    list_of_tuples = [] #list to hold all tuples
    for key, value in input_dict.items():
        list_of_tuples.append((key, value))
    return list_of_tuples

def sort_list_of_tuples(input_list_of_tuples): #Expects a list of tuples having format ('word', frequency) i.e ('the', 10)
    copy_list = input_list_of_tuples #Shallow copy for in place sorting
    copy_list.sort(key=lambda x: x[1], reverse=True) #In place sorting (reverse order)
    return copy_list

def print_first_n_tuples(input_list_of_tuples, num): #Expects a list of tuples of format (String, Integer) i.e. ('the', 10)                                                       # num - how many tuples to print
    counter = 0
    for tuple in input_list_of_tuples: #Linear pass through given list of tuples
        if (counter <= num):
            print("%s : %s" %(tuple[0], tuple[1]))
            counter += 1 #increment counter by 1
        else:
            return #Return once required num is reached

if __name__ == "__main__":
    input_file = input("Enter file name to read: ") #i.e. ./sample_text
    num = int(input("How many top frequency words do you want to print out? : "))
    input_dict = build_dict_of_words(input_file)

    list_of_tuples = build_list_of_tuples_from_dict(input_dict)

    sorted_list_of_tuples = sort_list_of_tuples(list_of_tuples) #In place sorting
    print_first_n_tuples(list_of_tuples, num) #Top 5 freuqncy words


