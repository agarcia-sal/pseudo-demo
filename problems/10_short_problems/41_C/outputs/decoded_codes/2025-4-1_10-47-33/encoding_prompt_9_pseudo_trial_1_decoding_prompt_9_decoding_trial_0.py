# Step 1: Receive Input
input_string = input().strip()  # Read the line and remove surrounding whitespace

# Step 2: Replace Word Aliases
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Adjust Beginning of String
if modified_string.startswith('.'):
    modified_string = "dot" + modified_string  # Prepend "dot" if string starts with "."

# Step 4: Initialize Counters
counter = 0  # Counter for occurrences of '@'
char_list = []  # List to store characters of modified string

# Step 5: Handle Special Cases for Starting Character
if modified_string.startswith('@'):
    modified_string = "at" + modified_string[1:]  # Replace the first character '@' with 'at'

# Step 6: Iterate through Each Character
for char in modified_string:
    if char == "@":
        if counter > 0:
            char_list.append("at")  # Append "at" if we've seen another "@"
            counter = 1  # Update counter for occurrences of "@"
        else:
            char_list.append("@")
            counter = 1  # Update counter for occurrences of "@"
    else:
        char_list.append(char)  # Append other characters directly

# Step 7: Combine List into String
final_string = ''.join(char_list)  # Join the list into a string

# Step 8: Adjust End of String
if final_string.endswith('.'):
    final_string = final_string[:-1] + "dot"  # Replace the last character '.' with 'dot'

# Step 9: Output Modified String
print(final_string)
