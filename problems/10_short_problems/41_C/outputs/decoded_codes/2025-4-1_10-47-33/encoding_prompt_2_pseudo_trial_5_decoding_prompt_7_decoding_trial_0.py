# Step 1: Read input from standard input and strip leading/trailing whitespace
input_text = input().strip()

# Step 2: Replace substrings 'dot' with '.' and 'at' with '@'
modified_text = input_text.replace("dot", ".").replace("at", "@")

# Step 3: Adjust beginning character if modified text starts with a '.'
if modified_text.startswith('.'):
    modified_text = 'dot' + modified_text

# Step 4: Initialize variables
at_counter = 0  # Counter for occurrences of '@'
final_output = []  # List to collect characters of the final output
length_of_text = 0  # Variable for tracking length of the text

# Step 5: Handle leading '@'
if modified_text.startswith('@'):
    modified_text = 'at' + modified_text

# Step 6: Iterate over each character in the modified text
for character in modified_text:
    if character == '@':
        if at_counter > 0:  # If this is not the first '@'
            final_output.append("at")  # Append 'at' for subsequent '@'
        else:  # If this is the first '@'
            final_output.append(character)  # Append the '@' character itself
        at_counter += 1  # Update the counter for '@'
    else:
        final_output.append(character)  # Append non-'@' characters directly

# Step 7: Join collected characters into a single string
final_string = ''.join(final_output)

# Step 8: Final adjustment if the last character is a '.'
if final_string.endswith('.'):
    final_string = final_string[:-1] + "dot"  # Replace the '.' with 'dot'

# Step 9: Output the result
print(final_string)  # Display final modified string
