# Read a line of input from the user and strip leading/trailing spaces
input_string = input().strip()

# Replace keywords with symbols
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Check for leading symbols and modify accordingly
if modified_string and modified_string[0] == ".":
    modified_string = "dot" + modified_string

# Initialize variables
at_count = 0
char_list = []
length = 0

# Check for leading "at" and modify accordingly
if modified_string and modified_string[0] == "@":
    modified_string = "at" + modified_string

# Process each character in the modified string
for char in modified_string:
    if char == "@":
        if at_count > 0:  # If there's already an "@" encountered
            char_list.append("at")
            at_count = 1
        else:
            char_list.append("@")
            at_count = 1
    else:
        char_list.append(char)

# Join the characters into a single string
final_string = ''.join(char_list)

# Check for trailing symbols and modify accordingly
if final_string and final_string[-1] == ".":
    final_string = final_string[:-1] + "dot"

# Output the final transformed string
print(final_string)
