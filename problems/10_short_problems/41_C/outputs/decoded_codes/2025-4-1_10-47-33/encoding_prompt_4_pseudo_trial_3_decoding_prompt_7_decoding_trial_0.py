# Start of the program

# Read input from standard input
userInput = input()
# Remove any leading or trailing whitespace from userInput
userInput = userInput.strip()

# Replace words with symbols
userInput = userInput.replace('dot', '.')
userInput = userInput.replace('at', '@')

# Ensure input does not start with a '.'
if userInput.startswith('.'):
    userInput = 'dot' + userInput[1:]

# Initialize variables
occurrenceCounter = 0
modifiedCharacters = []

# Ensure input does not start with an '@'
if userInput.startswith('@'):
    userInput = 'at' + userInput[2:]  # skipping '@' as it's being replaced

# Process each character in the userInput
for character in userInput:
    if character == '@':
        # Handle occurrences of '@'
        if occurrenceCounter > 0:
            modifiedCharacters.append('at')
            occurrenceCounter = 1
        else:
            modifiedCharacters.append('@')
            occurrenceCounter = 1
    else:
        modifiedCharacters.append(character)

# Join modified characters into a single string
modifiedOutput = ''.join(modifiedCharacters)

# Ensure output does not end with a '.'
if modifiedOutput.endswith('.'):
    modifiedOutput = modifiedOutput[:-1] + 'dot'

# Print the final modified output
print(modifiedOutput)

# End of the program
