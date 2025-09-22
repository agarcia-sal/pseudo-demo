# Step 1: Receive Input
input_string = input().strip()  # Remove leading or trailing spaces

# Step 2: Replace Specific Words
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Ensure Starting Character
if modified_string.startswith("."):
    modified_string = "dot" + modified_string

# Step 4: Initialize Variables
at_counter = 0
final_characters = []  # List to hold characters for final output

# Step 5: Check for Starting "at"
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]  # Change first character to "at"

# Step 6: Character Processing
for char in modified_string:
    if char == "@":
        if at_counter > 0:
            final_characters.append("at")  # Append "at" on subsequent occurrences
            at_counter = 1  # Ensure the counter is set
        else:
            final_characters.append("@")  # Append "@" for the first occurrence
            at_counter = 1  # Increase the counter
    else:
        final_characters.append(char)  # Append non-"at" characters directly

# Step 7: Join List to Form a String
final_string = ''.join(final_characters)

# Step 8: Ensure Valid Ending
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Replace last character with "dot"

# Step 9: Output Result
print(final_string)
