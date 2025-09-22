# Read input from the user, removing extra spaces around it
input_string = input().strip()

# Replace occurrences of 'dot' with '.' and 'at' with '@'
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Handle leading period
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]

# Initialize counter for '@' occurrences and an empty list for characters
at_counter = 0
processed_characters = []

# Handle leading '@' symbol
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]

# Process each character in the modified string
for character in modified_string:
    if character == "@":
        if at_counter > 0:
            processed_characters.append("at")  # Avoid duplicate '@'
            at_counter = 1
        else:
            processed_characters.append("@")
            at_counter = 1
    else:
        processed_characters.append(character)

# Join characters together into a single string
final_string = ''.join(processed_characters)

# Handle trailing period
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Output the final processed string
print(final_string)
