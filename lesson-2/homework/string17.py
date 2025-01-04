# Ask the user for a string and replace all the vowels with a symbol (e.g., *).

# Ask the user to input a string
user_string = input("Please enter a string: ")

# Specify the vowels
vowels = "aeiouAEIOU"

# Replace each vowel with the symbol '*'
replaced_string = ''.join('*' if char in vowels else char for char in user_string)

# Print the result
print("String after replacing vowels:", replaced_string)
