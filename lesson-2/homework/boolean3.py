# Write a program that checks if a number is positive and even

# Ask the user to input a number
num = int(input("Enter a number: "))

# Check if the number is positive and even
if num > 0 and num % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number is either not positive or not even.")
