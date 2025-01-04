# Write a program that accepts a username and password and checks if both are not empty.

# Ask the user to input a username
username = input("Enter your username: ")

# Ask the user to input a password
password = input("Enter your password: ")

# Check if both username and password are not empty
if username.strip() and password.strip():
    print("Username and password are valid.")
else:
    print("Username or password cannot be empty.")
