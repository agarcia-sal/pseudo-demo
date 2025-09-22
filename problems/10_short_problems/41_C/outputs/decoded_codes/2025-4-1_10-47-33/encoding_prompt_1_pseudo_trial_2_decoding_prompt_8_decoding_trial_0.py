# Read Input
userInput = input().strip()

# Replace Substrings
userInput = userInput.replace("dot", ".").replace("at", "@")

# Adjust Starting Character
if userInput.startswith("."):
    userInput = "dot" + userInput

# Initialize Variables
atCounter = 0
convertedCharacters = []
length = 0  # This variable is declared but not used

# Handle @ Character
if userInput.startswith("@"):
    userInput = "at" + userInput[1:]

# Process Each Character
for currentChar in userInput:
    if currentChar == "@":
        if atCounter > 0:
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
if result.endswith("."):
    result = result[:-1] + "dot"

# Output the Result
print(result)
