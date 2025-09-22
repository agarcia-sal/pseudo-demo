# Step 1: Read the input string and prepare it for processing
inputString = input().strip()  # Remove any leading/trailing whitespace

# Step 2: Replace specific substrings for formatting
inputString = inputString.replace("dot", ".")
inputString = inputString.replace("at", "@")

# Step 3: Check and modify the first character if it's a period
if inputString and inputString[0] == ".":  # Ensure the string is not empty
    inputString = "dot" + inputString[1:]  # Prepend "dot"

# Step 4: Initialize variables for processing the string
countAt = 0  # Counter for occurrences of '@' character
formattedCharacters = []  # To hold processed characters
length = 0  # This variable is initialized but not used subsequently

# Step 5: Modify the string further if it starts with '@'
if inputString and inputString[0] == "@":  # Ensure the string is not empty
    inputString = "at" + inputString[1:]  # Prepend "at"

# Step 6: Iterate through each character in the modified string
for character in inputString:
    if character == "@":
        if countAt > 0:
            formattedCharacters.append("at")
            countAt = 1
        else:
            formattedCharacters.append("@")
            countAt = 1
    else:
        formattedCharacters.append(character)

# Step 7: Join the formatted characters into a single string
outputString = ''.join(formattedCharacters)

# Step 8: Final formatting for the output string
if outputString and outputString[-1] == ".":  # Check if the string is not empty
    outputString = outputString[:-1] + "dot"  # Replace last character with "dot"

# Step 9: Output the final formatted string
print(outputString)
