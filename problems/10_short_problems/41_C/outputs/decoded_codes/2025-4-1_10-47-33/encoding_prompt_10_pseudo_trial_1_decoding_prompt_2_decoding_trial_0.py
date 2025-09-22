# BEGIN

# Step 1: Read input
input_line = input().strip()
input_line = input_line.replace('dot', '.')
input_line = input_line.replace('at', '@')

# Step 2: Handle leading dot
if input_line.startswith('.'):
    input_line = 'dot' + input_line[1:]

counter = 0
c = []  # Initialize empty list
length = 0  # Not used in pseudocode but initialized for completeness

# Step 3: Handle leading at sign
if input_line.startswith('@'):
    input_line = 'at' + input_line[1:]

# Step 4: Process each character of the input_line
for character in input_line:  # Iterate through each character
    if character == '@':
        if counter > 0:
            c.append('at')
            counter = 1
        else:
            c.append('@')
            counter = 1
    else:
        c.append(character)

# Step 5: Join list c into final string
final_output = ''.join(c)

# Step 6: Handle trailing dot
if final_output.endswith('.'):
    final_output = final_output[:-1] + 'dot'

# Step 7: Output the final result
print(final_output)

# END
