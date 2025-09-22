# Step 1: Receive Input
input_string = input()

# Step 2: Replace Placeholders
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Check Leading Character
if modified_string.startswith('.'):
    modified_string = "dot" + modified_string

# Step 4: Initialize Variables
at_counter = 0
output_characters = []
current_length = 0

# Step 5: Check for Leading At Symbol
if modified_string.startswith('@'):
    modified_string = "at" + modified_string

# Step 6: Process Each Character
for char in modified_string:
    if char == '@':
        if at_counter > 0:
            output_characters.append("at")
            at_counter = 0
        else:
            output_characters.append(char)
            at_counter = 1
    else:
        output_characters.append(char)

# Step 7: Construct Output String
output_string = ''.join(output_characters)

# Step 8: Check Trailing Character
if output_string.endswith('.'):
    output_string = output_string[:-1] + "dot"

# Step 9: Output Result
print(output_string)
