# Step 1: Read Input
userInput = input().strip()  # Read a line of input and strip whitespace

# Step 2: Replace Substrings
userInput = userInput.replace("dot", ".")  # Replace "dot" with "."
userInput = userInput.replace("at", "@")    # Replace "at" with "@"

# Step 3: Adjust Starting Character
if userInput.startswith("."):  # Check if first character is "."
    userInput = "dot" + userInput  # Prepend "dot"

# Step 4: Initialize Variables
atCounter = 0  # Initialize counter for "@" occurrences
convertedCharacters = []  # List to hold processed characters
length = 0  # Length variable, unused in this logic

# Step 5: Handle @ Character
if userInput.startswith("@"):  # Check if first character is "@"
    userInput = "at" + userInput[1:]  # Replace "@" with "at"

# Step 6: Process Each Character
for currentChar in userInput:  # Loop through each character in userInput
    if currentChar == "@":  # Check if current character is "@"
        if atCounter > 0:  # If "@" has been seen before
            convertedCharacters.append("at")  # Append "at"
            atCounter = 1  # Reset counter to 1
        else:
            convertedCharacters.append("@")  # Append "@"
            atCounter = 1  # Set counter to 1
    else:
        convertedCharacters.append(currentChar)  # Append current character

# Step 7: Combine Converted Characters
result = ''.join(convertedCharacters)  # Join characters to form final string

# Step 8: Final Adjustments
if result.endswith("."):  # Check if last character is "."
    result = result[:-1] + "dot"  # Replace "." with "dot"

# Step 9: Output the Result
print(result)  # Print the final result
