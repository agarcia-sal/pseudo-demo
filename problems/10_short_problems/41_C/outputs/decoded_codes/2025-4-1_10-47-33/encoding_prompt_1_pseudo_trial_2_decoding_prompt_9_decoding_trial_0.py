# Read Input
userInput = input().strip()  # Get input and remove leading/trailing whitespace

# Replace Substrings
userInput = userInput.replace("dot", ".")
userInput = userInput.replace("at", "@")

# Adjust Starting Character
if userInput and userInput[0] == ".":
    userInput = "dot" + userInput

# Initialize Variables
atCounter = 0
convertedCharacters = []

# Handle @ Character
if userInput and userInput[0] == "@":
    userInput = "at" + userInput[1:]

# Process Each Character
for currentChar in userInput:
    if currentChar == "@":
        if atCounter > 0:  # If "@" has been encountered before
            convertedCharacters.append("at")
            atCounter = 1
        else:
            convertedCharacters.append("@")
            atCounter = 1
    else:
        convertedCharacters.append(currentChar)

# Combine Converted Characters
result = ''.join(convertedCharacters)

# Final Adjustments
if result and result[-1] == ".":
    result = result[:-1] + "dot"

# Output the Result
print(result)
