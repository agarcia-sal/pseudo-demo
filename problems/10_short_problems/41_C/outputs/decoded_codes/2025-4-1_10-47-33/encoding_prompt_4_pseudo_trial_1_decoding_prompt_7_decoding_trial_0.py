# This program replaces specific words in a given input string, processes the string based on certain rules,
# and outputs the final modified string.

# Read input from the user
inputString = input()

# Replace words with symbols
inputString = inputString.replace('dot', '.')
inputString = inputString.replace('at', '@')

# Ensure the string starts with 'dot' if it begins with '.'
if inputString.startswith('.'):
    inputString = 'dot' + inputString[1:]

# Initialize variables for processing
countAtSymbol = 0  # Counter to track occurrences of '@'
processedCharacters = []  # List to hold processed characters
length = 0  # Initialize length variable (not used further)

# Ensure the string starts with 'at' if it begins with '@'
if inputString.startswith('@'):
    inputString = 'at' + inputString[1:]

# Process each character in the modified string
for character in inputString:
    if character == '@':
        # Check if the character '@' appears consecutively
        if countAtSymbol > 0:
            processedCharacters.append('at')  # Replace consecutive '@' with 'at'
            countAtSymbol = 1  # Reset counter
        else:
            processedCharacters.append('@')  # Append single '@'
            countAtSymbol = 1  # Increment counter
    else:
        processedCharacters.append(character)  # Append regular characters

# Join processed characters into a single string
resultString = ''.join(processedCharacters)

# Replace trailing '.' with 'dot'
if resultString.endswith('.'):
    resultString = resultString[:-1] + 'dot'  # Replace last character with 'dot'

# Output the final processed string
print(resultString)
