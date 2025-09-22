# Read input from the user and clean it
emailInput = input().strip()

# Replace substrings "dot" with "." and "at" with "@"
emailInput = emailInput.replace("dot", ".")
emailInput = emailInput.replace("at", "@")

# Ensure the first character rule
if emailInput.startswith('.'):
    emailInput = "dot" + emailInput

# Initialize state variables
previousAtCount = 0
outputCharacters = []

# Handle the '@' character
if emailInput.startswith('@'):
    emailInput = "at" + emailInput[1:]  # Replace the first character with "at"

# Process each character in the string
for currentCharacter in emailInput:
    if currentCharacter == '@':
        if previousAtCount > 0:
            outputCharacters.append("at")
            previousAtCount = 1
        else:
            outputCharacters.append('@')
            previousAtCount = 1
    else:
        outputCharacters.append(currentCharacter)

# Form the final output string
finalOutput = ''.join(outputCharacters)

# Ensure the final character rule
if finalOutput.endswith('.'):
    finalOutput = finalOutput[:-1] + "dot"

# Display the result
print(finalOutput)
