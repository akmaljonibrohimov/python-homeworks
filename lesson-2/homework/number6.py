# Create a program that accepts a number and returns the last digit of that number.

# Program to return the last digit of a number
def get_last_digit(number):
    return abs(number) % 10

# Input from the user
try:
    number = int(input("Enter a number: "))
    last_digit = get_last_digit(number)
    print(f"The last digit of {number} is {last_digit}.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")