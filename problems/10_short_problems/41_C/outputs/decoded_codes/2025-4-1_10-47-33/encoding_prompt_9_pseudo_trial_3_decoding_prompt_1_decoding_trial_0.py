# Step 1: Receive Input
input_string = input().strip()

# Step 2: Replace Text Patterns
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Adjust Leading Character
if modified_string.startswith("."):
    modified_string = "dot" + modified_string

# Step 4: Initialize Variables
counter = 0
char_list = []
# The length of the string could be tracked if needed, but it is not required in this context

# Step 5: Check for Leading "at"
if modified_string.startswith("@"):
    modified_string = "at" + modified_string

# Step 6: Iterate Through Each Character
for char in modified_string:
    if char == "@":
        if counter > 0:
            char_list.append("at")
            counter = 1
        else:
            char_list.append("@")
            counter = 1
    else:
        char_list.append(char)

# Step 7: Reconstruct the String
final_string = ''.join(char_list)

# Step 8: Adjust Trailing Character
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Step 9: Output the Result
print(final_string)
