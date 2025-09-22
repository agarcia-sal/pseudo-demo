# Read input from the user and trim whitespace
userInput = input().strip()

# Replace substrings as specified
userInput = userInput.replace("dot", ".").replace("at", "@")

# Check if the first character is a dot and prepend "dot" if necessary
if userInput.startswith("."):
    userInput = "dot" + userInput[1:]

# Initialize a counter and an empty list for characters
counter = 0
charList = []

# Check if the first character is "@" and prepend "at" if necessary
if userInput.startswith("@"):
    userInput = "at" + userInput[1:]

# Process each character in the userInput
for currentChar in userInput:
    if currentChar == "@":
        if counter > 0:
            charList.append("at")
            counter = 1
        else:
            charList.append(currentChar)
            counter = 1
    else:
        charList.append(currentChar)

# Join the processed characters into a final string result
finalResult = ''.join(charList)

# Check if the last character is a dot and modify the result accordingly
if finalResult.endswith("."):
    finalResult = finalResult[:-1] + "dot"

# Output the final result
print(finalResult)
