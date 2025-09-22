# This script processes a user input string for specific substitutions and character management

# Step 1: Read Input
userInput = input().strip()  # Read a line of input and remove whitespace

# Step 2: Replace Substrings
userInput = userInput.replace("dot", ".")  # Replace "dot" with "."
userInput = userInput.replace("at", "@")    # Replace "at" with "@"

# Step 3: Adjust Starting Character
if userInput.startswith("."):
    userInput = "dot" + userInput  # Prepend "dot" if it starts with "."

# Step 4: Initialize Variables
atCounter = 0  # Counter for "@" occurrences
convertedCharacters = []  # List to store processed characters

# Step 5: Handle @ Character
if userInput.startswith("@"):
    userInput = "at" + userInput[1:]  # Replace "@" with "at" at the starting position

# Step 6: Process Each Character
for currentChar in userInput:
    if currentChar == "@":
        if atCounter > 0:  # If "@" has already been seen
            convertedCharacters.append("at")  # Append "at"
            atCounter = 1  # Reset counter
        else:
            convertedCharacters.append("@")  # Append "@" to the list
            atCounter = 1  # Increment counter of "@" seen
    else:
        convertedCharacters.append(currentChar)  # Append current character

# Step 7: Combine Converted Characters
result = ''.join(convertedCharacters)  # Join list into a single string

# Step 8: Final Adjustments
if result.endswith("."):
    result = result[:-1] + "dot"  # Replace last char "." with "dot"

# Step 9: Output the Result
print(result)  # Output the final processed string
