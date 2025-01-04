# Create a program that takes a number and checks if it’s even or not.

# Program to check if a number is even or not
def is_even(number):
    return number % 2 == 0

# Input from the user
try:
    number = int(input("Enter a number: "))
    if is_even(number):
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")