# Create a program that accepts two strings and checks if they have the same length

# Ask the user to input the first string
string1 = input("Enter the first string: ")

# Ask the user to input the second string
string2 = input("Enter the second string: ")

# Check if the two strings have the same length
if len(string1) == len(string2):
    print("The two strings have the same length.")
else:
    print("The two strings do not have the same length.")
