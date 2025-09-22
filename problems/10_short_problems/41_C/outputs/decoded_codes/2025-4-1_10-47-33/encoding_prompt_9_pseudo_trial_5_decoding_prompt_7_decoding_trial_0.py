# Step 1: Receive Input
input_string = input().strip()  # Read user input and remove leading/trailing spaces

# Step 2: Replace Keywords
# Replace occurrences of "dot" with "." and "at" with "@"
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Check for Leading Symbols
if modified_string and modified_string[0] == '.':
    modified_string = "dot" + modified_string  # Prepend "dot" if the first character is "."

# Step 4: Initialize Variables
at_counter = 0  # Counter for occurrences of "@"
char_list = []  # List to hold processed characters
length = 0  # Initialize length variable (not used currently, but available for future use)

# Step 5: Check for Leading "at"
if modified_string and modified_string[0] == '@':
    modified_string = "at" + modified_string  # Prepend "at" if the first character is "@"

# Step 6: Process Each Character
for char in modified_string:
    if char == '@':
        if at_counter > 0:  # If another "@" was already encountered
            char_list.append("at")  # Append "at" to the list
            at_counter = 1  # Keep counter as 1
        else:
            char_list.append("@")  # Append "@" for the first occurrence
            at_counter = 1  # Mark that we have encountered "@"
    else:
        char_list.append(char)  # Append other characters directly to the list

# Step 7: Join Characters
final_string = ''.join(char_list)  # Combine the characters into a single string

# Step 8: Check Trailing Symbols
if final_string and final_string[-1] == '.':
    final_string = final_string[:-1] + "dot"  # Replace trailing "." with "dot"

# Step 9: Output the Result
print(final_string)  # Print the transformed string
