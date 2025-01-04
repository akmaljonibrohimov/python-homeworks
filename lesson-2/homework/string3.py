# Write a Python program to:

# Take a string input from the user.
# Print the length of the string.
# Convert the string to uppercase and lowercase.


# Program to manipulate a string input from the user
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

# Execute the function
string_operations()
