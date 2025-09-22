# Start of the program

# Read input from the user
userInput = input().strip()  # Remove leading and trailing spaces

# Replace occurrences of "dot" with "."
userInput = userInput.replace("dot", ".")
# Replace occurrences of "at" with "@"
userInput = userInput.replace("at", "@")

# Check if the first character is a dot
if userInput.startswith("."):
    userInput = "dot" + userInput[1:]  # Prepend "dot" to input, removing the leading dot

# Initialize the counter and character list
counter = 0
charList = []

# Check if the first character is an @ symbol
if userInput.startswith("@"):
    userInput = "at" + userInput[1:]  # Prepend "at" to input, removing the leading @

# Process each character in userInput
for currentChar in userInput:
    if currentChar == "@":  # Check if the character is '@'
        if counter > 0:
            charList.append("at")  # Append "at" if counter is greater than 0
            counter = 1  # Reset counter
        else:
            charList.append(currentChar)  # Append '@' character
            counter = 1  # Set counter to 1
    else:
        charList.append(currentChar)  # Append current character

# Create final result string by joining the character list
finalResult = ''.join(charList)

# Check if the last character of finalResult is a dot
if finalResult.endswith("."):
    finalResult = finalResult[:-1] + "dot"  # Remove last character and append "dot"

# Output the result
print(finalResult)

# End of the program
