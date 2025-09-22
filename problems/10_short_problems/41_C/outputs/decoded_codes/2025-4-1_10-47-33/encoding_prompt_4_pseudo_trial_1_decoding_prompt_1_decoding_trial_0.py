# BEGIN

# Read input from user
inputString = input()

# Replace words with symbols
inputString = inputString.replace('dot', '.')
inputString = inputString.replace('at', '@')

# Ensure the string starts with 'dot' if it begins with '.'
if inputString.startswith('.'):
    inputString = 'dot' + inputString[1:]

# Initialize variables for processing
countAtSymbol = 0
processedCharacters = []
length = 0  # This variable is not used further in the pseudocode, hence it can be omitted

# Ensure the string starts with 'at' if it begins with '@'
if inputString.startswith('@'):
    inputString = 'at' + inputString[1:]

# Process each character in the modified string
for character in inputString:
    if character == '@':
        # Check if the character '@' appears consecutively
        if countAtSymbol > 0:
            processedCharacters.append('at')
            countAtSymbol = 1
        else:
            processedCharacters.append('@')
            countAtSymbol = 1
    else:
        processedCharacters.append(character)

# Join processed characters into a single string
resultString = ''.join(processedCharacters)

# Replace trailing '.' with 'dot'
if resultString.endswith('.'):
    resultString = resultString[:-1] + 'dot'

# Output the final processed string
print(resultString)

# END
