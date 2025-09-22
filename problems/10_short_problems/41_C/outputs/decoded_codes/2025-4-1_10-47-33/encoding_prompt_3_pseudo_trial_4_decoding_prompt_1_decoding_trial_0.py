# Read input from standard input
inputString = input().strip()

# Replace occurrences of specific words with symbols
inputString = inputString.replace("dot", ".")
inputString = inputString.replace("at", "@")

# If the first character is '.', prepend 'dot' to the string
if inputString.startswith('.'):
    inputString = 'dot' + inputString[1:]

# Initialize a counter and an empty list to hold characters
counter = 0
characterList = []
length = 0

# If the first character is '@', prepend 'at' to the string
if inputString.startswith('@'):
    inputString = 'at' + inputString[1:]

# Process each character in inputString
for character in inputString:
    if character == '@':
        if counter > 0:
            characterList.append('at')
            counter = 1
        else:
            characterList.append('@')
            counter = 1
    else:
        characterList.append(character)

# Join the list of characters into a single string
processedString = ''.join(characterList)

# If the last character is '.', replace it with 'dot'
if processedString.endswith('.'):
    processedString = processedString[:-1] + 'dot'

# Output the final processed string
print(processedString)
