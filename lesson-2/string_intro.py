# ' - single quote  
# " - double quote
# \ - back slash
# / - forward slash
# \n - newline character
# \' - single quote
# \" - double quote
# \t - tab
# \\ - back slash
# \b - remove

hello = "Hello\nWor\bld"

word = "I\'m a \"teacher"
# print(word)
print(hello)







my_str = "Hello World" #Sequence
# print(len(my_str)) 

# Slicing or Indexing
# BEGIN:END:STEP
# print(my_str[:4] + my_str[5:])
# print(my_str[::2])

#        -1
my_str = "Hello World" #Sequence

# print(my_str[-5:])

# SyntaxError
# TypeError
# ValueError
# IndexError: string index out of range

# Mutable vs Immutable (O'zgaruvchan vs O'zgarmas)

my_str = "Apple"
print("Oldin:", id(my_str))

my_str2 = 'a' + my_str[1:]
print("Keyin:", id(my_str2))

print(my_str, my_str2)

# object.method()

