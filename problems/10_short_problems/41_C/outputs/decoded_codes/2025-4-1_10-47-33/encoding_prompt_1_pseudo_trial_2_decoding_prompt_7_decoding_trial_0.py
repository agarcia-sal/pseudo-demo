# Step 1: Read input from the user
userInput = input().strip()  # Remove leading and trailing whitespace

# Step 2: Replace substrings "dot" with "." and "at" with "@"
userInput = userInput.replace("dot", ".")
userInput = userInput.replace("at", "@")

# Step 3: Adjust starting character
if userInput and userInput[0] == ".":  # Ensure userInput is not empty
    userInput = "dot" + userInput

# Step 4: Initialize variables
atCounter = 0  # Counter for "@" occurrences
convertedCharacters = []  # List to hold processed characters

# Step 5: Handle @ character
if userInput and userInput[0] == "@":  # Ensure userInput is not empty
    userInput = "at" + userInput[1:]  # Replace "@" with "at"

# Step 6: Process each character
for currentChar in userInput:
    if currentChar == "@":
        if atCounter > 0:
            convertedCharacters.append("at")  # Append "at" if it's a duplicate
            atCounter = 1  # Reset counter since we've seen "at" again
        else:
            convertedCharacters.append("@")  # Append "@" for the first occurrence
            atCounter = 1  # Set counter to indicate we've seen "at"
    else:
        convertedCharacters.append(currentChar)  # Append current character if not "@"

# Step 7: Combine converted characters into a single string
result = ''.join(convertedCharacters)

# Step 8: Final adjustments
if result and result[-1] == ".":  # Check if the last character is "."
    result = result[:-1] + "dot"  # Replace last "." with "dot"

# Step 9: Output the result
print(result)
