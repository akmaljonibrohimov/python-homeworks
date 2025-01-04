# Write a program that takes two numbers and prints out the result of integer division and theremainder.

# Program to calculate integer division and remainder
def calculate_division_and_remainder(num1, num2):
    # Check for division by zero
    if num2 == 0:
        return None, "Division by zero is not allowed."

    quotient = num1 // num2
    remainder = num1 % num2
    return quotient, remainder

# Input from the user
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = calculate_division_and_remainder(num1, num2)
    if result[0] is None:
        print(result[1])
    else:
        quotient, remainder = result
        print(f"The result of integer division is {quotient} and the remainder is {remainder}.")
except ValueError:
    print("Invalid input. Please enter numeric values.")
