# Receive input from the user
input_string = input().strip()  # Read a line and remove leading/trailing whitespace

# Replace text representations with their actual characters
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Check and adjust starting character for special handling
if input_string and input_string[0] == ".":
    input_string = "dot" + input_string  # Prepend "dot" if string starts with "."

# Initialize variables
count = 0  # Counter for occurrences of "at"
characters = []  # List to store processed characters

# Check for '@' symbol at the start of the input
if input_string and input_string[0] == "@":
    characters.append("at")  # Prepend "at" if the string starts with "@"
    count = 1

# Process each character in the string
for currentCharacter in input_string:
    if currentCharacter == "@":
        if count > 0:  # If we have seen "at" already
            characters.append("at")  # Add "at" to the characters list
            count = 1  # Reset count to 1
        else:
            characters.append("@")  # Add "@" to the characters list
            count = 1  # Set count to 1 for the current "at"
    else:
        characters.append(currentCharacter)  # Add the current character to the list

# Join processed characters into a final string
final_string = ''.join(characters)

# Handle trailing periods
if final_string and final_string[-1] == ".":
    final_string = final_string[:-1] + "dot"  # Replace trailing "." with "dot"

# Output the final string
print(final_string)
