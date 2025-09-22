# Start the program.

# Read a line of input and remove any leading or trailing whitespace.
input_string = input().strip()

# Replace all occurrences of the string "dot" with the character '.' in the input.
modified_string = input_string.replace("dot", ".")

# Replace all occurrences of the string "at" with the character '@' in the input.
modified_string = modified_string.replace("at", "@")

# If the first character of the modified string is '.', do the following:
if modified_string.startswith('.'):
    # Prepend the string "dot" to the modified string, excluding the first character.
    modified_string = "dot" + modified_string[1:]

# Initialize a variable `count_at` to zero (to track occurrences of '@').
count_at = 0

# Initialize an empty list `output_characters` to store processed characters.
output_characters = []

# If the first character of the modified string is '@', do the following:
if modified_string.startswith('@'):
    # Prepend the string "at" to the modified string, excluding the first character.
    modified_string = "at" + modified_string[1:]

# For each character in the modified string:
for char in modified_string:
    # If the character is '@':
    if char == '@':
        # If `count_at` is greater than zero, append the string "at" to `output_characters` and set `count_at` to 1.
        if count_at > 0:
            output_characters.append("at")
            count_at = 1
        else:
            # Otherwise, append the character '@' to `output_characters` and set `count_at` to 1.
            output_characters.append('@')
            count_at = 1
    else:
        # If the character is not '@', directly append it to `output_characters`.
        output_characters.append(char)

# Combine all elements in `output_characters` into a single string named `final_output`.
final_output = ''.join(output_characters)

# If the last character of `final_output` is '.', do the following:
if final_output.endswith('.'):
    # Replace the last character with the string "dot".
    final_output = final_output[:-1] + "dot"

# Print the `final_output`.
print(final_output)

# End the program.
