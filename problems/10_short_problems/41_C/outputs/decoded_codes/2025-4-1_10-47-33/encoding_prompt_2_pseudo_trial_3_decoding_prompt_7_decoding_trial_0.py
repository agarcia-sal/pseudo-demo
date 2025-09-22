# Step 1: Read input and strip leading/trailing whitespace
input_string = input().strip()

# Step 2: Replace "dot" with "."
modified_string = input_string.replace("dot", ".")

# Step 3: Replace "at" with "@"
modified_string = modified_string.replace("at", "@")

# Step 4: Check if the first character is a period
if modified_string and modified_string[0] == '.':
    modified_string = "dot" + modified_string[1:]  # Prepend "dot", excluding the first character

# Step 5: Initialize counter and list for characters
at_counter = 0
char_list = []

# Step 6: Initialize current position (not used in this code)
current_position = 0

# Step 7: Check if the first character is an at symbol
if modified_string and modified_string[0] == '@':
    modified_string = "at" + modified_string[1:]  # Prepend "at", excluding the first character

# Step 8: Iterate through each character in modified string
for character in modified_string:
    if character == '@':
        # If we've seen "at" before, append "at" to list
        if at_counter > 0:
            char_list.append("at")
            at_counter = 1  # Reset the counter
        else:
            char_list.append('@')  # Append the @ symbol
            at_counter = 1  # Set the counter
    else:
        # If character is not '@', just append it
        char_list.append(character)
        at_counter = 0  # Reset counter for other characters
    
# Step 9: Join all elements in the list to form a single string
output_string = ''.join(char_list)

# Step 10: Check if the last character is a period
if output_string and output_string[-1] == '.':
    output_string = output_string[:-1] + "dot"  # Replace last character with "dot"

# Step 11: Output the modified string
print(output_string)
