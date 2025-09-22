# Receive Input
user_input = input()

# Replace Keywords with Symbols
modified_string = user_input.replace("dot", ".").replace("at", "@")

# Check for Leading Character
if modified_string and modified_string[0] == ".":
    modified_string = "dot" + modified_string

# Initialize Variables
at_counter = 0
processed_characters = []

# Check for Leading "at"
if modified_string and modified_string[0] == "@":
    processed_characters.append("at")
    at_counter = 1
else:
    processed_characters.append(modified_string[0])

# Iterate Over Each Character in the String
for char in modified_string[1:]:
    if char == "@":
        if at_counter > 0:
            processed_characters.append("at")
            at_counter = 1  # Ensure only one "at" is appended in consecutive cases
        else:
            processed_characters.append("@")
            at_counter = 1  # Increment counter since we added an "@"
    else:
        processed_characters.append(char)
        at_counter = 0  # Reset counter for non-"at" characters

# Join Processed Characters
final_string = ''.join(processed_characters)

# Check for Trailing Character
if final_string and final_string[-1] == ".":
    final_string = final_string[:-1] + "dot"  # Replace trailing dot with "dot"

# Output the Result
print(final_string)
