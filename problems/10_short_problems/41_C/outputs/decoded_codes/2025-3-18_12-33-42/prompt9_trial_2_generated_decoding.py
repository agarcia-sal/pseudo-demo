# Step 1: Receive Input
input_string = input()

# Step 2: Initial Replacements
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 3: Check First Character
if input_string.startswith("."):
    input_string = "dot" + input_string

# Step 4: Initialize Variables
counter = 0  # Tracks consecutive "at" symbols
output_characters = []  # List for processed characters
length = 0  # Not specifically used in the original code

# Step 5: Handle Leading "At" Symbol
if input_string.startswith("@"):
    input_string = "at" + input_string

# Step 6: Process Each Character
for current_character in input_string:
    if current_character == "@":
        if counter > 0:  # Already encountered "at"
            output_characters.append("at")
        else:
            output_characters.append("@")
        counter = 1  # Indicate "at" has been processed
    else:
        output_characters.append(current_character)
        counter = 0  # Reset counter for other characters

# Step 7: Reconstruct Output String
final_output = ''.join(output_characters)

# Step 8: Final Character Check
if final_output.endswith("."):
    final_output = final_output[:-1] + "dot"  # Replace last dot with "dot"

# Step 9: Display Result
print(final_output)
