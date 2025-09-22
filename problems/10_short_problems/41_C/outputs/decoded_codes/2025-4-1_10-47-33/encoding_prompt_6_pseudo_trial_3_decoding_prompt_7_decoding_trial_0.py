# Begin the program
# Read a line of input and remove any surrounding whitespace
inputLine = input().strip()  # Read input and strip whitespace

# Replace occurrences of 'dot' with '.' and 'at' with '@'
inputLine = inputLine.replace('dot', '.')
inputLine = inputLine.replace('at', '@')

# If the modified input starts with a '.', prepend 'dot' to it
if inputLine.startswith('.'):
    inputLine = 'dot' + inputLine

# Initialize a count for consecutive '@' symbols
consecutiveAtCount = 0
outputCharacters = []  # Initialize an empty list for characters

# If the modified input starts with '@', prepend 'at' to it
if inputLine.startswith('@'):
    inputLine = 'at' + inputLine

# Iterate through each character in the modified input
for character in inputLine:
    
    # Check if the character is '@'
    if character == '@':
        # If it is the second consecutive '@', append 'at' to the list
        if consecutiveAtCount > 0:
            outputCharacters.append('at')  # Replace consecutive '@' with 'at'
            consecutiveAtCount = 1  # Count consecutive '@'
        else:
            outputCharacters.append('@')  # Append the first '@'
            consecutiveAtCount = 1  # Count first '@'
    else:
        # If it is not '@', append the character to the list
        outputCharacters.append(character)
        consecutiveAtCount = 0  # Reset count for non-'@' characters

# Join all characters in the outputCharacters list into a string
modifiedText = ''.join(outputCharacters)

# If the last character in the modified text is '.', replace it with 'dot'
if modifiedText.endswith('.'):
    modifiedText = modifiedText[:-1] + 'dot'  # Replace the last character with 'dot'

# Print the final modified text
print(modifiedText)
