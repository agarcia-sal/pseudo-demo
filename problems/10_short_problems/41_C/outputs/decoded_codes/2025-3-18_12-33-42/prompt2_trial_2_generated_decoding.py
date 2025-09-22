# Start of the process

# Input Handling
input_string = input().strip()  # Read input and remove leading/trailing whitespace
input_string = input_string.replace("dot", ".")  # Replace "dot" with "."
input_string = input_string.replace("at", "@")  # Replace "at" with "@"

# Initial Adjustment
if input_string and input_string[0] == ".":
    input_string = "dot" + input_string[1:]  # Prepend "dot" starting from the second character

# Initialization
counter = 0  # Track occurrence of "@"
characterList = []  # Holds characters or strings
length = 0  # Initialized but not used later

# Further Input Adjustment
if input_string and input_string[0] == "@":
    input_string = "at" + input_string[1:]  # Prepend "at" starting from the second character

# Character Processing
for char in input_string:
    if char == "@":
        if counter > 0:  # Check if "@" has already been encountered
            characterList.append("at")  # Append "at"
            counter = 1  # Keeping count
        else:
            characterList.append("@")  # Append single "@"
            counter = 1  # Set counter to indicate the presence of "@"
    else:
        characterList.append(char)  # Append the character directly

# Reconstructing the Output
finalString = ''.join(characterList)  # Join all elements into a single string

# Final Adjustment
if finalString and finalString[-1] == ".":
    finalString = finalString[:-1] + "dot"  # Replace last character with "dot"

# Output Result
print(finalString)  # Print the final string

# End of the process
