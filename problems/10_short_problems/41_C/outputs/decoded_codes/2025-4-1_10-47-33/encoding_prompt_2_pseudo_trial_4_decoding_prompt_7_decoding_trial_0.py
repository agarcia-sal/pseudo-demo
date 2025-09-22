# Step 1: Read a line of input and remove leading or trailing spaces
input_string = input().strip()

# Step 2: Replace 'dot' with '.' and 'at' with '@'
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Check if the first character is a period and handle accordingly
if modified_string and modified_string[0] == '.':
    modified_string = "dot" + modified_string  # Add 'dot' at the beginning

# Step 4: Initialize counter for '@' occurrences and a list for building the final string
at_counter = 0
final_chars = []

# Step 5: Handle the first character if it's an '@'
if modified_string and modified_string[0] == '@':
    modified_string = "at" + modified_string[1:]  # Replace '@' with 'at' at the beginning

# Step 6: Iterate through each character in the modified string
for char in modified_string:
    if char == "@":
        # If '@' was added before, append 'at' to the list
        if at_counter > 0:
            final_chars.append("at")
        else:
            final_chars.append("@")  # Append '@' and update counter
            at_counter += 1
    else:
        final_chars.append(char)  # Append any character that is not '@'

# Step 7: Join all characters in final_chars into a single string
final_string = ''.join(final_chars)

# Step 8: Check if the last character is a period and handle it
if final_string and final_string[-1] == '.':
    final_string = final_string[:-1] + "dot"  # Replace '.' with 'dot'

# Step 9: Output the final modified string
print(final_string)
