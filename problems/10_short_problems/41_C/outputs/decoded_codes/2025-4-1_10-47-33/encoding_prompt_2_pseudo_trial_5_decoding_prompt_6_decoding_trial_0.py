# Step 1: Read input and trim whitespace
input_text = input().strip()

# Step 2: Replace substrings in the input text
modified_text = input_text.replace("dot", ".").replace("at", "@")

# Step 3: Adjust beginning character if it starts with a period
if modified_text.startswith('.'):
    modified_text = "dot" + modified_text[1:]

# Step 4: Initialize variables
at_counter = 0  # Counter for occurrences of '@'
final_characters = []  # List to collect characters for final output
text_length = len(modified_text)  # Get the length of the modified text

# Step 5: Handle leading '@' in the modified text
if modified_text.startswith('@'):
    final_characters.append("at")
    final_characters.append(modified_text[1:])
    at_counter += 1
else:
    final_characters.append(modified_text)

# Step 6: Iterate over each character in the modified text
for character in modified_text:
    if character == '@':
        if at_counter > 0:
            final_characters.append("at")  # Append "at" for subsequent '@'
        else:
            final_characters.append(character)  # Append the first '@'
            at_counter += 1  # Update the counter
    else:
        final_characters.append(character)  # Append character if it's not '@'

# Step 7: Join characters into a single string
final_string = ''.join(final_characters)

# Step 8: Final adjustment for trailing period
if final_string.endswith('.'):
    final_string = final_string[:-1] + "dot"

# Step 9: Output the final result
print(final_string)
