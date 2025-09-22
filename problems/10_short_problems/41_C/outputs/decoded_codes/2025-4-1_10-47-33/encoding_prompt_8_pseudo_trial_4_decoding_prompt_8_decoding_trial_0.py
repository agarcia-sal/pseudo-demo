# Step 1: Read Input
input_string = input().strip()

# Step 2: Replace Specific Words
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Handle Leading Period
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]

# Step 4: Initialize Variables
at_counter = 0
output_characters = []

# Step 5: Handle Leading At-Symbol
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]

# Step 6: Process Each Character
for char in modified_string:
    if char == "@":
        if at_counter > 0:
            output_characters.append("at")
            at_counter = 1
        else:
            output_characters.append("@")
            at_counter = 1
    else:
        output_characters.append(char)

# Step 7: Join Characters Together
final_string = ''.join(output_characters)

# Step 8: Handle Trailing Period
if final_string.endswith('.'):
    final_string = final_string[:-1] + "dot"

# Step 9: Output the Result
print(final_string)
