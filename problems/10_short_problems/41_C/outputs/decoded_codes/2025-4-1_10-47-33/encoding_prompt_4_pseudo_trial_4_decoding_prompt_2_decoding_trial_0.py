# Read input from standard input
inputString = input()

# Remove leading and trailing whitespace
inputString = inputString.strip()

# Replace 'dot' with '.' and 'at' with '@'
inputString = inputString.replace('dot', '.')
inputString = inputString.replace('at', '@')

# If the first character is '.', prepend 'dot'
if inputString.startswith('.'):
    inputString = 'dot' + inputString[1:]

# Initialize variables
countAt = 0
resultCharacters = []
length = 0

# If the first character is '@', prepend 'at'
if inputString.startswith('@'):
    inputString = 'at' + inputString[1:]

# Loop through each character in the modified inputString
for character in inputString:
    if character == '@':
        # If '@' has been encountered before, append 'at' instead of another '@'
        if countAt > 0:
            resultCharacters.append('at')
            countAt = 1
        else:
            resultCharacters.append('@')
            countAt = 1
    else:
        # Add non-'@' characters to result
        resultCharacters.append(character)

# Join the list of characters to form the final output string
finalString = ''.join(resultCharacters)

# Handle trailing '.' in the final string by replacing it with 'dot'
if finalString.endswith('.'):
    finalString = finalString[:-1] + 'dot'

# Print the resulting string
print(finalString)
