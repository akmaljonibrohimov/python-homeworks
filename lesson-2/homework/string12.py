# Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., - or ,).


# Ask the user to input a list of words (comma-separated)
words = input("Please enter a list of words, separated by spaces: ").split()

# Ask the user for a character to use as a separator
separator = input("Enter a character to use as a separator: ")

# Join the words into a single string, separated by the chosen character
joined_string = separator.join(words)

# Print the result
print("Joined string:", joined_string)

# Example Usage:

# Input:
# Please enter a list of words, separated by spaces: apple banana cherry
# Enter a character to use as a separator: -

# Output:
# Joined string: apple-banana-cherry

