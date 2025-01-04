# Create a program to ask name and year of birth from user and tell them their age.

# Program to calculate age based on name and year of birth
def calculate_age(year_of_birth):
    from datetime import datetime
    current_year = datetime.now().year
    return current_year - year_of_birth

# Input from the user
try:
    name = input("Enter your name: ")
    year_of_birth = int(input("Enter your year of birth: "))
    age = calculate_age(year_of_birth)
    print(f"Hello {name}, you are {age} years old.")
except ValueError:
    print("Invalid input. Please enter a valid year of birth.")
