# Step 1: Read Input
userInput = input().strip()

# Step 2: Replace Text Representations
userInput = userInput.replace("dot", ".")
userInput = userInput.replace("at", "@")

# Step 3: Check and Correct Starting Character
if userInput.startswith("."):
    userInput = "dot" + userInput

# Step 4: Initialize Variables
atCount = 0
formattedChars = []
length = 0  # This variable is not used in further logic

# Step 5: Check and Correct Starting with "at"
if userInput.startswith("@"):
    userInput = "at" + userInput

# Step 6: Build Formatted String
for currentChar in userInput:
    if currentChar == "@":
        if atCount > 0:
            formattedChars.append("at")
            atCount = 1
        else:
            formattedChars.append("@")
            atCount = 1
    else:
        formattedChars.append(currentChar)

# Step 7: Join Characters into a String
finalOutput = ''.join(formattedChars)

# Step 8: Check and Correct Ending Character
if finalOutput.endswith("."):
    finalOutput = finalOutput[:-1] + "dot"

# Step 9: Output Result
print(finalOutput)
