# Step 1: Read input and remove leading/trailing whitespace
input_string = input().strip()

# Step 2: Replace occurrences of "dot" with "."
modified_string = input_string.replace("dot", ".")

# Step 3: Replace occurrences of "at" with "@"
modified_string = modified_string.replace("at", "@")

# Step 4: Check if the first character is a period
if modified_string and modified_string[0] == '.':
    modified_string = "dot" + modified_string[1:]  # prepend "dot" excluding the first character

# Step 5: Initialize counter for occurrences of "@" and an empty list
at_counter = 0
result_list = []

# Step 6: Initialize current position (not necessarily used as per instructions)
current_position = 0

# Step 7: Check if the first character is an "@"
if modified_string and modified_string[0] == '@':
    modified_string = "at" + modified_string[1:]  # prepend "at" excluding the first character

# Step 8: Iterate over each character in the modified string
for character in modified_string:
    if character == '@':
        if at_counter > 0:  # If we have seen "@" before
            result_list.append("at")
            at_counter = 1  # Reset counter since we are appending "at"
        else:
            result_list.append('@')
            at_counter = 1  # Set counter to indicate "@" has been seen
    else:
        result_list.append(character)  # Append the character as it is

# Step 9: Join all elements in the list to form a single string
final_string = ''.join(result_list)

# Step 10: Check if the last character is a period
if final_string and final_string[-1] == '.':
    final_string = final_string[:-1] + "dot"  # Replace last character with "dot"

# Step 11: Output the modified string
print(final_string)
