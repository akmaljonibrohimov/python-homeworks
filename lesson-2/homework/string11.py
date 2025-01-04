# Write a program to check if a string contains any digits.

# Ask the user to input a string
user_input = input("Please enter a string: ")

# Check if the string contains any digits
contains_digits = any(char.isdigit() for char in user_input)

# Print the result
if contains_digits:
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")
