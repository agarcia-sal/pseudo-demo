# Step 1: Read input from standard input
input_line = input().strip()  # Strip whitespace from the input

# Replace 'dot' with '.' and 'at' with '@'
input_line = input_line.replace('dot', '.').replace('at', '@')

# Step 2: Handle leading dot
if input_line.startswith('.'):
    input_line = 'dot' + input_line[1:]  # Add 'dot' at the beginning if it starts with a dot

counter = 0  # Initialize a counter
characters_list = []  # Initialize an empty list to hold characters
length = 0  # Initialize length variable

# Step 3: Handle leading at sign
if input_line.startswith('@'):
    input_line = 'at' + input_line[1:]  # Add 'at' at the beginning if it starts with an at sign

# Step 4: Process each character of the input_line
for character in input_line:
    if character == '@':  # Check if the character is '@'
        if counter > 0:
            characters_list.append('at')  # Append 'at' to the list
            counter = 1  # Increment counter
        else:
            characters_list.append('@')  # Append '@' to the list
            counter = 1  # Increment counter
    else:
        characters_list.append(character)  # Append the character to the list

# Step 5: Join list characters_list into final string
final_output = ''.join(characters_list)  # Join the characters into a single string

# Step 6: Handle trailing dot
if final_output.endswith('.'):
    final_output = final_output[:-1] + 'dot'  # Replace trailing dot with 'dot'

# Step 7: Output the final result
print(final_output)  # Print the final output
