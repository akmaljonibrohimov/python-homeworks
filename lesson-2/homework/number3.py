# Create a program that converts kilometers to meters and centimeters.

def convert_kilometrs(kilometers):
    # conversion factors
    meters = kilometers * 1000
    centimeters = kilometers * 100000
    
    return meters, centimeters

# Input from the user 
try:
    kilometers = float(input("Enter the distance in kilometers: "))
    if kilometers < 0 :
        print("Distance cannot be negative. Please enter a valid number.")
    else:
        meters, centimeters = convert_kilometrs(kilometers)
        print(f"{kilometers} kilometers is equivalent to {meters} meters and {centimeters} centimeters.")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
