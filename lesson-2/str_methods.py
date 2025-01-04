# Case sensitive vs Case Insensitive

fruit = "apple banana"
print('Orginal:', fruit)

print(fruit.lower())
print(fruit.upper())
print(fruit.capitalize())
print(fruit.title())

print(fruit.endswith('a'))
print(fruit.startswith('b'))  

print('-'*50)
word = '     Hello World  '
print(word)
print(word.strip())

print('-'*50)

fruits = 'apple banana cherry'
print(fruits.split(" "))

print('-'*50)
file_name = "numeric.py"
base_name = file_name.split('.')[0]
extension = file_name.split('.')[1]
print(f"{file_name=}")
print(f"{base_name=}")
print(f"{extension=}")