# Write a program that asks the user for a string and prints the first and last characters of the string.


# Ask the user to input a string
user_input = input("Please enter a string: ")

# Check if the string is not empty
if len(user_input) > 0:
    # Print the first and last characters
    print("First character:", user_input[0])
    print("Last character:", user_input[-1])
else:
    print("The string is empty.")
