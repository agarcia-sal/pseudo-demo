# Start
# Read input from the user and trim any leading or trailing spaces
userInput = input().strip()

# Replace substrings
userInput = userInput.replace("dot", ".")
userInput = userInput.replace("at", "@")

# Check beginning character
if userInput.startswith("."):
    userInput = "dot" + userInput[1:]

# Initialize variables
counter = 0
charList = []

# Check for starting character
if userInput.startswith("@"):
    userInput = "at" + userInput[1:]

# Process each character in userInput
for currentChar in userInput:
    if currentChar == "@":
        if counter > 0:
            charList.append("at")
            counter = 1
        else:
            charList.append("@")
            counter = 1
    else:
        charList.append(currentChar)

# Join characters
finalResult = ''.join(charList)

# Check ending character
if finalResult.endswith("."):
    finalResult = finalResult[:-1] + "dot"

# Output result
print(finalResult)
# End
