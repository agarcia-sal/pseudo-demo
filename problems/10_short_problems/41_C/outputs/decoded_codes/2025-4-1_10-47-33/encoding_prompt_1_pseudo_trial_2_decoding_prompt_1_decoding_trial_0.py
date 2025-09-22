# Step 1: Read Input
userInput = input().strip()

# Step 2: Replace Substrings
userInput = userInput.replace("dot", ".").replace("at", "@")

# Step 3: Adjust Starting Character
if userInput and userInput[0] == ".":
    userInput = "dot" + userInput

# Step 4: Initialize Variables
atCounter = 0
convertedCharacters = []
length = 0  # Note: length is unused

# Step 5: Handle @ Character
if userInput and userInput[0] == "@":
    userInput = "at" + userInput[1:]

# Step 6: Process Each Character
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

# Step 7: Combine Converted Characters
result = ''.join(convertedCharacters)

# Step 8: Final Adjustments
if result and result[-1] == ".":
    result = result[:-1] + "dot"

# Step 9: Output the Result
print(result)
