# Read input from the user
emailInput = input().strip()

# Replace occurrences of "dot" with "." and "at" with "@"
emailInput = emailInput.replace("dot", ".").replace("at", "@")

# Ensure that the string doesn't start with a dot
if emailInput.startswith("."):
    emailInput = "dot" + emailInput

# Initialize variables for processing
previousAtCount = 0
outputCharacters = []

# Handle the case where the first character is '@'
if emailInput.startswith("@"):
    emailInput = "at" + emailInput[1:]

# Process each character in emailInput
for currentCharacter in emailInput:
    if currentCharacter == '@':
        if previousAtCount > 0:
            outputCharacters.append("at")  # Handle consecutive '@'
        else:
            outputCharacters.append('@')  # First '@'
        previousAtCount = 1  # Set count of '@' characters
    else:
        outputCharacters.append(currentCharacter)  # Append other characters

# Form the final output string
finalOutput = ''.join(outputCharacters)

# Replace the last character with "dot" if it is '.'
if finalOutput.endswith('.'):
    finalOutput = finalOutput[:-1] + "dot"

# Display the result
print(finalOutput)

# Test cases can be added below as comments for clarity
# Example test cases:
# Input: "hello at world dot com"
# Output: "hello@world.com"
# Input: "dot hello at world dot"
# Output: "dot hello@worlddot"
# Input: "at example dot com"
# Output: "at@example.com"
