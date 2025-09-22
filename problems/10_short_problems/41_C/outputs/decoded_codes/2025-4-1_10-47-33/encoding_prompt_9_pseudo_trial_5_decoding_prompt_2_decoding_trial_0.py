# Step 1: Receive Input
input_string = input().strip()

# Step 2: Replace Keywords
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Check for Leading Symbols
if modified_string.startswith("."):
    modified_string = "dot" + modified_string

# Step 4: Initialize Variables
counter = 0
char_list = []
length = 0

# Step 5: Check for Leading "at"
if modified_string.startswith("@"):
    modified_string = "at" + modified_string

# Step 6: Process Each Character
for character in modified_string:
    if character == "@":
        if counter > 0:  # Another "@" has been encountered
            char_list.append("at")
            counter = 1  # Resetting the counter
        else:
            char_list.append("@")
            counter += 1  # Incrementing the counter
    else:
        char_list.append(character)

# Step 7: Join Characters
final_string = ''.join(char_list)

# Step 8: Check Trailing Symbols
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Step 9: Output the Result
print(final_string)
