# Step 1: Read input and remove leading/trailing whitespace
input_string = input().strip()

# Step 2: Replace occurrences of "dot" with "."
modified_string = input_string.replace("dot", ".")

# Step 3: Replace occurrences of "at" with "@"
modified_string = modified_string.replace("at", "@")

# Step 4: Check if the first character is a period
if modified_string and modified_string[0] == '.':
    modified_string = "dot" + modified_string[1:]

# Step 5: Initialize counter for occurrences of the at symbol and an empty list for characters
at_counter = 0
char_list = []

# Step 6: Initialize current position (not used in this version but kept for structure)
current_position = 0 

# Step 7: Check if the first character is an at symbol
if modified_string and modified_string[0] == '@':
    modified_string = "at" + modified_string[1:]

# Step 8: Iterate through each character in the modified string
for character in modified_string:
    if character == '@':
        if at_counter > 0:
            char_list.append("at")
            at_counter = 1
        else:
            char_list.append('@')
            at_counter = 1
    else:
        char_list.append(character)

# Step 9: Join all elements in the list to form a single string
final_string = ''.join(char_list)

# Step 10: Check if the last character is a period
if final_string and final_string[-1] == '.':
    final_string = final_string[:-1] + "dot"

# Step 11: Output the modified string
print(final_string)
