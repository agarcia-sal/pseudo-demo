# Step 1: Read a line of input from the user and remove leading/trailing whitespace
input_line = input().strip()

# Step 2: Replace all occurrences of "dot" with "."
modified_input = input_line.replace("dot", ".")

# Step 3: Replace all occurrences of "at" with "@"
modified_input = modified_input.replace("at", "@")

# Step 4: If the first character is a period, prepend "dot" excluding the period
if modified_input.startswith('.'):
    modified_input = 'dot' + modified_input[1:]

# Step 5: Initialize counter for "@" occurrences
co = 0

# Step 6: Create an empty list to store characters of the final output
c = []

# Step 7: If the first character is an "@" symbol, prepend "at" excluding the "@" symbol
if modified_input.startswith('@'):
    modified_input = 'at' + modified_input[1:]

# Step 8: Iterate over each character in modified input
for char in modified_input:
    # Step 8a: If the character is "@"
    if char == '@':
        if co > 0:
            # Append "at" to the list
            c.append("at")
            co = 1  # Update counter to 1
        else:
            # Append "@" to the list
            c.append("@")
            co = 1  # Update counter to 1
    # Step 8b: If the character is not "@"
    else:
        c.append(char)

# Step 9: Join all elements of list c into a single string
final_output = ''.join(c)

# Step 10: If the last character is a period, remove it and append "dot"
if final_output.endswith('.'):
    final_output = final_output[:-1] + 'dot'

# Step 11: Output the final processed string
print(final_output)
