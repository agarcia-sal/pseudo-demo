# Start Process

# Receive Input
rawInput = input().strip()  # Read a line of input and remove surrounding spaces

# Replace Keywords
rawInput = rawInput.replace("dot", ".")  # Replace occurrences of 'dot' with '.'
rawInput = rawInput.replace("at", "@")    # Replace occurrences of 'at' with '@'

# Check for Leading Dot
if rawInput.startswith('.'):
    rawInput = 'dot' + rawInput[1:]  # Prepend 'dot' if it starts with '.'

# Initialize Variables
symbolTracker = 0  # Counter for tracking the last seen symbol
formattedCharacters = []  # List to hold the formatted characters

# Check for Leading At
if rawInput.startswith('@'):
    rawInput = 'at' + rawInput[1:]  # Prepend 'at' if it starts with '@'

# Process Each Character in Input
for currentCharacter in rawInput:
    if currentCharacter == '@':
        if symbolTracker > 0:  # Check if already processed an '@'
            formattedCharacters.append("at")  # Append 'at' to the list
            symbolTracker = 1
        else:
            formattedCharacters.append('@')  # Append the actual '@' symbol
            symbolTracker = 1
    else:
        formattedCharacters.append(currentCharacter)  # Append regular characters

# Join Formatted Characters
finalOutput = ''.join(formattedCharacters)  # Combine into a single string

# Check for Trailing Dot
if finalOutput.endswith('.'):
    finalOutput = finalOutput[:-1] + "dot"  # Replace trailing '.' with 'dot'

# Output Result
print(finalOutput)  # Print the final formatted output

# End of Process
