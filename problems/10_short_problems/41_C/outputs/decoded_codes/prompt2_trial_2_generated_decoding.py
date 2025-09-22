# Step 1: Define Input
input_string = input().strip()

# Step 2: Replace Substrings
modified_input = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Handle Leading Period
if modified_input.startswith("."):
    modified_input = "dot" + modified_input[1:]

# Step 4: Initialize Variables
co = 0
c = []
l = 0  # l is initialized but not used in this pseudocode

# Step 5: Handle Leading "At" Symbol
if modified_input.startswith("@"):
    modified_input = "at" + modified_input[1:]

# Step 6: Iterate Through Each Character
for i in modified_input:
    if i == "@":
        if co > 0:  # If "@" has already been added
            c.append("at")
            co = 1
        else:  # First "@" encountered
            c.append("@")
            co = 1
    else:  # If the character is not "@"
        c.append(i)

# Step 7: Combine Characters
final_string = ''.join(c)

# Step 8: Handle Trailing Period
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Step 9: Output Result
print(final_string)
