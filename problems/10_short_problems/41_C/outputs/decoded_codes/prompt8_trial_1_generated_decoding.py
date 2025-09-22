# Start Program

# Read Input
user_input = input().strip()

# Replace Text Representations
modified_string = user_input.replace("dot", ".").replace("at", "@")

# Check Leading Character
if modified_string.startswith("."):
    modified_string = "dot" + modified_string

# Initialize Counters and Collectors
counter = 0
collected_characters = []

# Handle Leading "@" Character
if modified_string.startswith("@"):
    modified_string = "at" + modified_string

# Iterate Through Characters
for char in modified_string:
    if char == "@":
        if counter > 0:
            collected_characters.append("at")
            counter = 1
        else:
            collected_characters.append("@")
            counter = 1
    else:
        collected_characters.append(char)

# Join Collected Characters
final_string = ''.join(collected_characters)

# Check Trailing Character
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Output the Result
print(final_string)

# End Program
