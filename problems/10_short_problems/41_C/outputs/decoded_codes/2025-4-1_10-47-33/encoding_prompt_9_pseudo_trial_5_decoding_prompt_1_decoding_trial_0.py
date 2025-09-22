# Step 1: Receive Input
input_string = input().strip()

# Step 2: Replace Keywords
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Check for Leading Symbols
if modified_string and modified_string[0] == ".":
    modified_string = "dot" + modified_string

# Step 4: Initialize Variables
at_counter = 0
characters = []
length = 0  # This variable is defined but not utilized in this code. 

# Step 5: Check for Leading "at"
if modified_string and modified_string[0] == "@":
    modified_string = "at" + modified_string

# Step 6: Process Each Character
for character in modified_string:
    if character == "@":
        if at_counter > 0:
            characters.append("at")
            at_counter = 1
        else:
            characters.append("@")
            at_counter = 1
    else:
        characters.append(character)

# Step 7: Join Characters
final_string = ''.join(characters)

# Step 8: Check Trailing Symbols
if final_string and final_string[-1] == ".":
    final_string = final_string[:-1] + "dot"

# Step 9: Output the Result
print(final_string)
