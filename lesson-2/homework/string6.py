# Write a Python program to check if one string contains another.

# Program to manipulate a string input from the user, check if it's a palindrome, count vowels and consonants, and check substring presence
def string_operations():
    user_input = input("Enter a string: ")
    
    # Print the length of the string
    string_length = len(user_input)
    print(f"Length of the string: {string_length}")

    # Convert to uppercase
    uppercase_string = user_input.upper()
    print(f"Uppercase: {uppercase_string}")

    # Convert to lowercase
    lowercase_string = user_input.lower()
    print(f"Lowercase: {lowercase_string}")

    # Check if the string is a palindrome
    cleaned_input = ''.join(filter(str.isalnum, user_input)).lower()
    if cleaned_input == cleaned_input[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

    # Count vowels and consonants
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowel_count = sum(1 for char in user_input.lower() if char in vowels)
    consonant_count = sum(1 for char in user_input.lower() if char in consonants)
    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}")

    # Check if one string contains another
    substring = input("Enter a substring to check: ")
    if substring in user_input:
        print(f"The string contains the substring '{substring}'.")
    else:
        print(f"The string does not contain the substring '{substring}'.")

# Execute the function
string_operations()
