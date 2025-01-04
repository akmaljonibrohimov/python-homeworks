# Write a program that checks if a string starts with one word and ends with another.
# Example:

# Input: "Python is fun!"
# Starts with: "Python"
# Ends with: "fun!"


# Ask the user to input a string
user_string = input("Please enter a string: ")

# Ask for the word the string should start with
start_word = input("Enter the word it should start with: ")

# Ask for the word the string should end with
end_word = input("Enter the word it should end with: ")

# Check if the string starts with the start_word and ends with the end_word
starts_with = user_string.startswith(start_word)
ends_with = user_string.endswith(end_word)

# Print the results
if starts_with and ends_with:
    print(f'The string starts with "{start_word}" and ends with "{end_word}".')
elif starts_with:
    print(f'The string starts with "{start_word}" but does not end with "{end_word}".')
elif ends_with:
    print(f'The string does not start with "{start_word}" but ends with "{end_word}".')
else:
    print(f'The string neither starts with "{start_word}" nor ends with "{end_word}".')


# input:

# Please enter a string: Python is fun!
# Enter the word it should start with: Python
# Enter the word it should end with: fun!

# Output:

# The string starts with "Python" and ends with "fun!".

