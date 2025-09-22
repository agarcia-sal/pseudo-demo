# Step 1: Read input and strip whitespace.
input_string = input().strip()

# Step 2: Replace "dot" with "." in the input string.
modified_string = input_string.replace("dot", ".")

# Step 3: Replace "at" with "@" in the modified string.
modified_string = modified_string.replace("at", "@")

# Step 4: Check if the first character is a period.
if modified_string and modified_string[0] == ".":
    modified_string = "dot" + modified_string[1:]

# Step 5: Initialize the counter for "at" occurrences and the list.
at_counter = 0
output_list = []

# Step 6: Initialize current position (not specifically used in this logic).
current_position = 0

# Step 7: Check if the first character is an "at" symbol.
if modified_string and modified_string[0] == "@":
    modified_string = "at" + modified_string[1:]

# Step 8: Process each character in the modified string.
for char in modified_string:
    if char == '@':
        if at_counter > 0:
            output_list.append("at")
        else:
            output_list.append("@")
        at_counter = 1
    else:
        output_list.append(char)
        at_counter = 0

# Step 9: Join the elements in the list to form a single string.
final_string = ''.join(output_list)

# Step 10: Check if the last character is a period.
if final_string and final_string[-1] == ".":
    final_string = final_string[:-1] + "dot"

# Step 11: Output the modified string.
print(final_string)
