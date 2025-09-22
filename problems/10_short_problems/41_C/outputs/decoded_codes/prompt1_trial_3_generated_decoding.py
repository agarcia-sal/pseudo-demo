# BEGIN

# Read input from the user
userInput = input()

# Replace all occurrences of 'dot' with '.' in the input string
userInput = userInput.replace('dot', '.')

# Replace all occurrences of 'at' with '@' in the modified string
userInput = userInput.replace('at', '@')

# If the string starts with '.', prepend 'dot' to the rest of the string
if userInput.startswith('.'):
    userInput = 'dot' + userInput[1:]

# Set counter to 0
counter = 0
# Initialize empty list called outputCharacters
outputCharacters = []

# If the string starts with '@', prepend 'at' to the rest of the string
if userInput.startswith('@'):
    userInput = 'at' + userInput[2:]

# Loop through each character in the modified string
for character in userInput:
    if character == '@':
        # If '@' already encountered, append 'at' to output
        if counter > 0:
            outputCharacters.append('at')
            counter = 1
        else:
            # First occurrence of '@', append it as is
            outputCharacters.append('@')
            counter = 1
    else:
        # Append the current character to output
        outputCharacters.append(character)

# Combine the list of characters back into a single string
finalOutput = ''.join(outputCharacters)

# If the final string ends with '.', replace it with 'dot'
if finalOutput.endswith('.'):
    finalOutput = finalOutput[:-1] + 'dot'

# Print the final processed string
print(finalOutput)

# END
