# Read Input
userInput = input().strip()  # remove leading/trailing whitespace

# Replace Substrings
userInput = userInput.replace("dot", ".")
userInput = userInput.replace("at", "@")

# Adjust Starting Character
if userInput.startswith("."):
    userInput = "dot" + userInput

# Initialize Variables
atCounter = 0
convertedCharacters = []

# Handle '@' Character
if userInput.startswith("@"):
    userInput = "at" + userInput[1:]  # Replace '@' with 'at'

# Process Each Character
for currentChar in userInput:
    if currentChar == "@":
        if atCounter > 0:
            convertedCharacters.append("at")
        else:
            convertedCharacters.append("@")
        atCounter = 1  # Mark that we've seen an '@'
    else:
        convertedCharacters.append(currentChar)

# Combine Converted Characters
result = ''.join(convertedCharacters)

# Final Adjustments
if result.endswith("."):
    result = result[:-1] + "dot"

# Output the Result
print(result)
