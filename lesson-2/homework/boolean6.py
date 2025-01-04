# Create a program that accepts a number and checks if it’s divisible by both 3 and 5

# Ask the user to input a number
num = int(input("Enter a number: "))

# Check if the number is divisible by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")
