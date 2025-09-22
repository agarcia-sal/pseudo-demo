# Receive Input
input_string = input().strip()  # Read and trim the input string

# Replace Specific Strings
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Check Beginning of String
if modified_string and modified_string[0] == '.':
    modified_string = "dot" + modified_string[1:]

# Initialize Variables
at_count = 0
collected_characters = []
char_index = 0

# Handle Starting Character
if modified_string and modified_string[0] == '@':
    modified_string = "at" + modified_string[1:]

# Iterate Through Characters
for char in modified_string:
    if char == '@':
        if at_count > 0:  # If 'at' has occurred before
            collected_characters.append("at")
        else:  # First occurrence of '@'
            collected_characters.append('@')
        at_count += 1
    else:
        collected_characters.append(char)

# Combine Collected Characters
final_string = ''.join(collected_characters)

# Final Adjustment
if final_string and final_string[-1] == '.':
    final_string = final_string[:-1] + "dot"  # Replace last '.' with 'dot'

# Output the Result
print(final_string)
