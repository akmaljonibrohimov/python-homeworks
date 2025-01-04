# Write a Python file that asks for three numbers and outputs the largest and smallest.


num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
num3=int(input("Enter third number : "))

# max

if num1>=num2 and num1>=num3:
    largest=num1
elif num2>=num1 and num2>=num3:
    largest=num2
else:
    largest=num3
print("The largest number is:",largest)


# min

if num1<=num2 and num1<=num3:
    smallest=num1
elif num2<=num1 and num2<=num3:
    smallest=num2
else:
    smallest=num3
print("The smallest number is:",smallest)


# Ex:

# Enter first number: 12
# Enter second number : 13
# Enter third number : 14

# Result:

# The largest number is: 14
# The smallest number is: 12











