# Step 1: Read input and trim spaces
input_string = input().strip()

# Step 2: Replace "dot" with "."
modified_input = input_string.replace("dot", ".")

# Step 3: Replace "at" with "@"
modified_input = modified_input.replace("at", "@")

# Step 4: Check first character for "."
if modified_input and modified_input[0] == ".":
    modified_input = modified_input[0] + "dot" + modified_input[1:]

# Step 5: Initialize counter for occurrences of "@"
at_counter = 0

# Step 6: Create a list to hold the final characters of the output
output_list = []

# Step 7: Variable for length (not used)
length = 0

# Step 8: Check first character for "@"
if modified_input and modified_input[0] == "@":
    modified_input = modified_input[0] + "at" + modified_input[1:]

# Step 9: Iterate through characters in modified input
for char in modified_input:
    if char == "@":
        if at_counter > 0:
            output_list.append("at")
            at_counter = 1
        else:
            output_list.append("@")
            at_counter = 1
    else:
        output_list.append(char)

# Step 10: Join all elements in the output_list into a final string
final_output = ''.join(output_list)

# Step 11: Check last character for "."
if final_output and final_output[-1] == ".":
    final_output = final_output[:-1] + "dot"

# Step 12: Output the final modified string
print(final_output)
