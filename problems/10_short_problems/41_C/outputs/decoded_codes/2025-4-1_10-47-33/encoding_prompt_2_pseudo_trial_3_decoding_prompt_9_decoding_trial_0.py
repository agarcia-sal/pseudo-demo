# Begin by reading a line of input and removing leading or trailing whitespace
input_string = input().strip()

# Step 2: Replace every occurrence of "dot" with "." in the input string
modified_string = input_string.replace("dot", ".")

# Step 3: Replace every occurrence of "at" with "@" in the modified string
modified_string = modified_string.replace("at", "@")

# Step 4: Check if the first character is a period. If it is, prepend "dot"
if modified_string and modified_string[0] == '.':
    modified_string = 'dot' + modified_string[1:]

# Step 5: Initialize a counter for occurrences of the "@" symbol and an empty list
at_counter = 0
result_list = []

# Step 6: Initialize a variable for the current position (not used further)
current_position = 0

# Step 7: Check if the first character is "@". If it is, prepend "at"
if modified_string and modified_string[0] == '@':
    modified_string = 'at' + modified_string[1:]

# Step 8: Process each character in the modified string
for char in modified_string:
    if char == '@':
        if at_counter > 0:
            result_list.append("at")
            at_counter = 1  # Reset the counter after appending "at"
        else:
            result_list.append('@')
            at_counter = 1  # Increment the counter the first time
    else:
        result_list.append(char)

# Step 9: Join all elements in the list to form a single string
final_string = ''.join(result_list)

# Step 10: Check if the last character is a period and replace with "dot"
if final_string and final_string[-1] == '.':
    final_string = final_string[:-1] + "dot"

# Step 11: Output the modified string
print(final_string)
