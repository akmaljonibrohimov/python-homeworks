# Make a program that converts a given Celsius temperature to Fahrenheit.

# Program to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Input from the user
try:
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} Celsius is equivalent to {fahrenheit} Fahrenheit.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")