# Receive Input: Read a line of text and strip leading/trailing whitespace
input_string = input().strip()

# Replace "dot" with "." and "at" with "@" in the input string
input_string = input_string.replace("dot", ".").replace("at", "@")

# Check and Adjust Starting Character
if input_string.startswith("."):
    input_string = "dot" + input_string  # Prepend "dot" if the string starts with "."

# Initialize Variables
count = 0  # Counter for occurrences of "at"
characters = []  # List to store processed characters

# Check for '@' Symbol at Start
if input_string.startswith("@"):
    characters.append("at")  # Prepend "at" if the string starts with "@"
    count = 1

# Process Each Character in the String
for current_character in input_string:
    if current_character == "@":
        if count > 0:
            characters.append("at")  # Add "at" representation if count is greater than zero
            count = 1  # Reset count
        else:
            characters.append("@")  # Add "@" symbol
            count = 1  # Set count to 1
    else:
        characters.append(current_character)  # Add the current character to the list

# Join Processed Characters
final_string = ''.join(characters)

# Handle Trailing Periods
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Replace the last "." with "dot"

# Output the Final String
print(final_string)
