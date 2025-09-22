# Begin Code

# Read input from the user
inputString = input()

# Replace occurrences of 'dot' with '.' and 'at' with '@'
inputString = inputString.replace('dot', '.')
inputString = inputString.replace('at', '@')

# Check if the first character is a dot
if inputString.startswith('.'):
    # Prepend 'dot' to the string
    inputString = 'dot' + inputString[1:]

# Initialize the counter for '@' occurrences
occurrenceCounter = 0
# Initialize an empty list to collect characters
characterList = []

# Check if the first character is '@'
if inputString.startswith('@'):
    # Prepend 'at' to the string
    inputString = 'at' + inputString[1:]

# Loop through each character in the modified input string
for character in inputString:
    # Check if the character is '@'
    if character == '@':
        # If '@' has already occurred before
        if occurrenceCounter > 0:
            # Append 'at' to the list
            characterList.append('at')
            occurrenceCounter = 1  # Update counter
        else:
            # Append '@' to the list
            characterList.append('@')
            occurrenceCounter = 1  # Update counter
    else:
        # Append the character to the list
        characterList.append(character)

# Join the list of characters into a single string
resultString = ''.join(characterList)

# Check if the last character is a dot
if resultString.endswith('.'):
    # Replace the last '.' with 'dot'
    resultString = resultString[:-1] + 'dot'

# Print the final modified string
print(resultString)

# End Code
