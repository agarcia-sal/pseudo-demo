# Begin the program

# Read input from the user
inputString = input()

# Replace occurrences of 'dot' with '.'
inputString = inputString.replace('dot', '.')

# Replace occurrences of 'at' with '@'
inputString = inputString.replace('at', '@')

# If the first character is '.', prepend 'dot'
if inputString.startswith('.'):
    inputString = 'dot' + inputString[1:]

# Initialize a counter for '@' symbols and a list for building the output
atCounter = 0
outputList = []

# If the first character is '@', prepend 'at'
if inputString.startswith('@'):
    inputString = 'at' + inputString[1:]

# Iterate through each character in the updated inputString
for character in inputString:
    # Check if the character is '@'
    if character == '@':
        # If '@' has already been added once, replace it with 'at'
        if atCounter > 0:
            outputList.append('at')
            atCounter = 1  # Mark '@' has been added again
        else:
            outputList.append('@')
            atCounter = 1  # Mark first '@' has been added
            
    else:
        # For other characters, add them directly to the outputList
        outputList.append(character)

# Join the list of characters into a single string
finalOutput = ''.join(outputList)

# If the last character is '.', replace it with 'dot'
if finalOutput.endswith('.'):
    finalOutput = finalOutput[:-1] + 'dot'

# Print the final transformed output
print(finalOutput)

# End the program
