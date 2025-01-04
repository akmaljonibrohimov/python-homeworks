# Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.

# Ask the user to input a string
user_string = input("Please enter a string: ")

# Ask the user to input a character to remove
char_to_remove = input("Please enter a character to remove: ")

# Remove all occurrences of the specified character from the string
updated_string = user_string.replace(char_to_remove, "")

# Print the result
print("String after removal:", updated_string)
