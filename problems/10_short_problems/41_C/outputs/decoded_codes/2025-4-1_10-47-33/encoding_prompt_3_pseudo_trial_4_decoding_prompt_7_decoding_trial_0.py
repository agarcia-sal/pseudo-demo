# Read input from standard input
inputString = input().strip()  # Remove leading and trailing whitespace

# Replace occurrences of specific words with symbols
inputString = inputString.replace("dot", ".")  # Replace "dot" with "."
inputString = inputString.replace("at", "@")    # Replace "at" with "@"

# If the first character is '.', prepend 'dot' to the string
if inputString.startswith('.'):
    inputString = 'dot' + inputString[1:]

# Initialize a counter and an empty list to hold characters
counter = 0
characterList = []  # List to hold processed characters

# Process each character in inputString
for character in inputString:
    if character == '@':
        if counter > 0:
            characterList.append('at')  # Append 'at' if we already counted one '@'
            counter = 1  # Reset counter
        else:
            characterList.append('@')  # Append single '@' for the first occurrence
            counter = 1  # Set counter to indicate we've seen '@'
    else:
        characterList.append(character)  # Append other characters directly

# Join the list of characters into a single string
processedString = ''.join(characterList)

# If the last character is '.', replace it with 'dot'
if processedString.endswith('.'):
    processedString = processedString[:-1] + 'dot'  # Replace last '.' with 'dot'

# Output the final processed string
print(processedString)
