# Extract car names from this text: txt = 'LMaasleitbtui'

# Program to extract car names from a scrambled text
def extract_car_names(scrambled_text):
    car_names = ['Lamborghini', 'Maserati', 'Bentley', 'Audi']
    extracted_cars = [car for car in car_names if all(char in scrambled_text for char in car)]
    return extracted_cars

# Example text
scrambled_text = 'LMaasleitbtui'
car_list = extract_car_names(scrambled_text)
print(f"Extracted car names: {', '.join(car_list) if car_list else 'None found'}")