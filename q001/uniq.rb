#Program to test if all characters in a string are unique

puts "Enter a string to check character uniqueness.."
str = gets.chomp!

def check_character_uniqueness(str)
  return str.chars.count === str.chars.uniq.count
end

puts check_character_uniqueness(str) ? "All Characters in String are Unique!" : "Not Unique!"
