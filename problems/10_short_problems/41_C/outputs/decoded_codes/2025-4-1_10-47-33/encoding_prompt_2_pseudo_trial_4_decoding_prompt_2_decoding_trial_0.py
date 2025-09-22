# Step 1: Read a line of input
input_string = input()

# Step 2: Remove any leading or trailing spaces
modified_string = input_string.strip()

# Step 3: Replace all occurrences of "dot" with "."
modified_string = modified_string.replace("dot", ".")

# Step 4: Replace all occurrences of "at" with "@"
modified_string = modified_string.replace("at", "@")

# Step 5: Check if the first character is a period
if modified_string.startswith('.'):
    modified_string = 'dot' + modified_string  # Add "dot" at the beginning

# Step 6: Initialize a counter for occurrences of "@" and an empty list to store characters
at_counter = 0
result_chars = []

# Step 7: Initialize a variable for the length of the string (not actively used)
string_length = len(modified_string)

# Step 8: Check if the first character is "@"
if modified_string.startswith('@'):
    modified_string = 'at' + modified_string[1:]  # Replace it with "at"

# Step 9: For each character in the modified string
for char in modified_string:
    if char == '@':
        # If "@" has already been added (counter > 0)
        if at_counter > 0:
            result_chars.append('at')  # Append "at" to the list
        else:
            result_chars.append('@')  # Append "@" to the list
            at_counter += 1  # Update the counter
    else:
        result_chars.append(char)  # Append the character to the list

# Step 10: Join all characters in the list into a single string
final_string = ''.join(result_chars)

# Step 11: Check if the last character is a period
if final_string.endswith('.'):
    final_string = final_string[:-1] + 'dot'  # Replace period with "dot"

# Step 12: Output the final modified string
print(final_string)
