# Ask the user for a sentence and create an acronym from the first letters of each word.
# Example:

# Input: "World Health Organization"
# Output: "WHO"


# Ask the user to input a sentence
sentence = input("Please enter a sentence: ")

# Split the sentence into words and create an acronym from the first letters
acronym = ''.join(word[0].upper() for word in sentence.split())

# Print the acronym
print("Acronym:", acronym)
