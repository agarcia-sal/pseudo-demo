# Read input text
input_text = input().strip()

# Replace substrings
input_text = input_text.replace("dot", ".")
input_text = input_text.replace("at", "@")

# Adjust beginning character
if input_text.startswith('.'):
    input_text = "dot" + input_text[1:]

# Initialize variables
at_counter = 0
final_output = []
text_length = len(input_text)

# Handle leading '@'
if input_text.startswith('@'):
    final_output.append("at")
    final_output.append('@')
    at_counter += 1
else:
    # Add if not leading '@'
    for char in input_text:
        if char == '@':
            # If this is not the first '@'
            if at_counter > 0:
                final_output.append("at")
            final_output.append('@')
            at_counter += 1
        else:
            final_output.append(char)

# Join characters to form the modified string
modified_string = ''.join(final_output)

# Final adjustment if the last character is a period
if modified_string.endswith('.'):
    modified_string = modified_string[:-1] + "dot"

# Output the final modified string
print(modified_string)
