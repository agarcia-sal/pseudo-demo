# Step 1: Read Input
user_input = input().strip()

# Step 2: String Replacement
modified_input = user_input.replace("dot", ".").replace("at", "@")

# Step 3: Handle Leading Period
if modified_input.startswith("."):
    modified_input = "dot" + modified_input[1:]

# Step 4: Initialize Tracking Variables
at_counter = 0
modified_chars = []

# Step 5: Handle Leading "@" Symbol
if modified_input.startswith("@"):
    modified_input = "at" + modified_input[1:]

# Step 6: Process Each Character
for char in modified_input:
    if char == "@":
        if at_counter > 0:
            modified_chars.append("at")
            at_counter = 1
        else:
            modified_chars.append("@")
            at_counter = 1
    else:
        modified_chars.append(char)

# Step 7: Join Characters into a String
final_string = ''.join(modified_chars)

# Step 8: Handle Trailing Period
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Step 9: Output Result
print(final_string)
