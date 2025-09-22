# Receive Input
input_string = input().strip()

# Replace Text Patterns
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Adjust Leading Character
if modified_string.startswith("."):
    modified_string = "dot" + modified_string

# Initialize Variables
at_counter = 0
char_list = []
string_length = len(modified_string)

# Check for Leading "at"
if modified_string.startswith("@"):
    modified_string = "at" + modified_string

# Iterate Through Each Character
for character in modified_string:
    if character == "@":
        if at_counter > 0:
            char_list.append("at")
            at_counter = 1
        else:
            char_list.append(character)
            at_counter = 1
    else:
        char_list.append(character)

# Reconstruct the String
final_string = ''.join(char_list)

# Adjust Trailing Character
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Output the Result
print(final_string)
