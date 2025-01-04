# Write a program that checks if the sum of two numbers is greater than 50.8. Create a program that checks if a given number is between 10 and 20 (inclusive)


# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the sum of the two numbers is greater than 50.8
if num1 + num2 > 50.8:
    print("The sum of the two numbers is greater than 50.8.")
else:
    print("The sum of the two numbers is not greater than 50.8.")

# Ask the user to input a number
num = float(input("Enter a number: "))

# Check if the number is between 10 and 20 (inclusive)
if 10 <= num <= 20:
    print("The number is between 10 and 20 (inclusive).")
else:
    print("The number is not between 10 and 20.")
