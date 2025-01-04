# Program to manipulate a string input from the user and check if it's a palindrome
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

# Execute the function
string_operations()
