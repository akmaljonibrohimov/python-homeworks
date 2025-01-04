# Write a program that asks the user for a sentence and prints the number of words in it.

# Ask the user to input a sentence
sentence = input("Please enter a sentence: ")

# Split the sentence into words and count the number of words
word_count = len(sentence.split())

# Print the number of words
print("Number of words:", word_count)