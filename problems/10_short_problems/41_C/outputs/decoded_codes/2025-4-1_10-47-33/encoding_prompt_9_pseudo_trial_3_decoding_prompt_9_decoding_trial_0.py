# Receive Input
input_string = input().strip()  # Read input and remove surrounding whitespace

# Replace Text Patterns
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Adjust Leading Character
if modified_string and modified_string[0] == ".":
    modified_string = "dot" + modified_string

# Initialize Variables
counter = 0  # To track occurrences of "@"
char_list = []  # To store characters

# Check for Leading "at"
if modified_string and modified_string[0] == "@":
    modified_string = "at" + modified_string

# Iterate Through Each Character
for character in modified_string:
    if character == "@":
        if counter > 0:
            char_list.append("at")
            counter = 1
        else:
            char_list.append(character)
            counter = 1
    else:
        char_list.append(character)

# Reconstruct the String
final_string = ''.join(char_list)

# Adjust Trailing Character
if final_string and final_string[-1] == ".":
    final_string = final_string[:-1] + "dot"

# Output the Result
print(final_string)
