#Program to check if string contains all unique characters

str = input("Enter string to check character uniqueness: ")  # input sample "abcdef" (with quotes)
print str


def check_character_uniqueness(str):
  #Check if all characters in a string are unique or not
  #return true only if all characters in string are unique
  return len(set(str)) == len(str)

#print check_character_uniqueness(str)

print "All characters in string are unique!" if check_character_uniqueness(str) else "Not Unique!"
