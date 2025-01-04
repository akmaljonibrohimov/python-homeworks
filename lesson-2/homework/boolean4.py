# Write a program that takes three numbers and checks if all of them are different

# Ask the user to input three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Check if all three numbers are different
if num1 != num2 and num1 != num3 and num2 != num3:
    print("All three numbers are different.")
else:
    print("Not all numbers are different.")
