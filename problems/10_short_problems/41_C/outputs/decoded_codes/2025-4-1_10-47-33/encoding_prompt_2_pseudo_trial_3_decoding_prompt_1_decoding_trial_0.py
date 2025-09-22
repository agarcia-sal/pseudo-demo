# Step 1: Read input and strip whitespace
input_string = input().strip()

# Step 2: Replace "dot" with "." and "at" with "@"
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Check if first character is a period
if modified_string and modified_string[0] == '.':
    modified_string = "dot" + modified_string[1:]

# Step 5: Initialize counter and list
at_counter = 0
result_list = []

# Step 7: Check if first character is an @ symbol
if modified_string and modified_string[0] == '@':
    result_list.append("at")
    result_list.append(modified_string[1:])
else:
    result_list.append(modified_string)

# Step 8: Loop through characters in modified string
for char in result_list[0]:  # result_list[0] is our modified string
    if char == '@':
        if at_counter > 0:
            result_list.append("at")
            at_counter = 1
        else:
            result_list.append('@')
            at_counter = 1
    else:
        result_list.append(char)

# Step 9: Join elements in list
final_string = ''.join(result_list)

# Step 10: Check if last character is a period
if final_string and final_string[-1] == '.':
    final_string = final_string[:-1] + "dot"

# Step 11: Output the modified string
print(final_string)
