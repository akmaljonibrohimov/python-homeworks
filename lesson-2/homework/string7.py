# Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.
# Example:

# Input sentence: "I love apples."
# Replace: "apples"
# With: "oranges"
# Output: "I love oranges."


# Ask for user input
sentence = input("Enter a sentence: ")
word_to_replace = input("Enter the word you want to replace: ")
replacement_word = input("Enter the word to replace with: ")

# Replace the word in the sentence
updated_sentence = sentence.replace(word_to_replace, replacement_word)

# Print the updated sentence
print("Updated sentence:", updated_sentence)