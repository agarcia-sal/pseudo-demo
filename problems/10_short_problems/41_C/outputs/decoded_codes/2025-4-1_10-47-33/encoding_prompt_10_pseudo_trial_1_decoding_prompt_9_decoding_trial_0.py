# Start of the program

# Step 1: Read input
input_line = input().strip()  # Read and strip whitespace from input
input_line = input_line.replace('dot', '.')  # Replace 'dot' with '.'
input_line = input_line.replace('at', '@')  # Replace 'at' with '@'

# Step 2: Handle leading dot
if input_line.startswith('.'):
    input_line = 'dot' + input_line[1:]  # Prepend 'dot' if it starts with a dot

counter = 0
c = []  # Initialize an empty list to store characters
length = 0  # Not used further in the pseudocode, but initialized

# Step 3: Handle leading at sign
if input_line.startswith('@'):
    input_line = 'at' + input_line[1:]  # Prepend 'at' if it starts with an at sign

# Step 4: Process each character in the input_line
for character in input_line:
    if character == '@':
        if counter > 0:
            c.append('at')  # Append 'at' if it's the second or more '@'
            counter = 1  # Reset counter
        else:
            c.append('@')  # Append '@' for the first occurrence
            counter = 1  # Set counter to 1 indicating an '@' was found
    else:
        c.append(character)  # Append the current character to list c

# Step 5: Join list c into final string
final_output = ''.join(c)  # Join the characters in list c into a single string

# Step 6: Handle trailing dot
if final_output.endswith('.'):
    final_output = final_output[:-1] + 'dot'  # Replace trailing '.' with 'dot'

# Step 7: Output the final result
print(final_output)  # Print the final output

# End of program
