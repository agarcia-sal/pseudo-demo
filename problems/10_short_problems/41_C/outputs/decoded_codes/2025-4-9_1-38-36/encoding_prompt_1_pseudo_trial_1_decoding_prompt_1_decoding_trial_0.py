# Step 1: Read Input
user_input = input().strip()

# Step 2: Modify Keywords
modified_input = user_input.replace("dot", ".").replace("at", "@")

# Step 3: Check for Leading Dot
if modified_input and modified_input[0] == ".":
    modified_input = "dot" + modified_input

# Step 4: Initialize Variables
counter = 0
result = []

# Step 5: Handle Leading At Symbol
if modified_input and modified_input[0] == "@":
    result.append("at")
    counter = 1

# Step 6: Process Each Character
for character in modified_input:
    if character == "@":
        if counter > 0:
            result.append("at")
            counter = 1
        else:
            result.append("@")
            counter = 1
    else:
        result.append(character)

# Step 7: Convert List to String
final_string = ''.join(result)

# Step 8: Check Trailing Dot
if final_string and final_string[-1] == ".":
    final_string = final_string[:-1] + "dot"

# Step 9: Output Result
print(final_string)
