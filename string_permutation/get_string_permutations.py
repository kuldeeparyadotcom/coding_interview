#!/usr/local/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

def get_permutations(input_str): #Expects a strig of unique characters
    """
    Returns set of all the permutatios of the given string of unique characters
    """
    permutations = set() #Empty set to hold final permutations
    
    len_input_str = len(input_str) #We may need it further in program

    if len_input_str < 1: #Base case
        return permutations

    if len_input_str == 1: #Base Case
        permutations.add(input_str)
        return permutations

    #Recursion case
    first_char = input_str[0] #Get first character
    input_str = input_str[1:] #Get first character out of original input_str for further recursive calls
    perms = get_permutations(input_str)

    for item in perms: #each item in permutaion set of remaining string
        for ind in range(len(perms)+1): #Insert first character at each and every index possible
            perm = item[:ind] + first_char + item[ind:] #Insert first character at index ind
            permutations.add(perm) #Include in permutations set
    
    return permutations

if __name__ == "__main__":
    input_str = input("Enter a string of unique character to get its' all permuations: ")
    permutations = get_permutations(input_str)
    print("*"*15)
    for p in permutations:
        print(p)
    print("*"*15)
    print("Total permutations of %s: %s" %(input_str, len(permutations)))

