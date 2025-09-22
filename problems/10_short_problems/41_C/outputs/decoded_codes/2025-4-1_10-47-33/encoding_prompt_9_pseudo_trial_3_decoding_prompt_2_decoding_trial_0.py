# Step 1: Receive Input
input_text = input().strip()

# Step 2: Replace Text Patterns
input_text = input_text.replace("dot", ".")
input_text = input_text.replace("at", "@")

# Step 3: Adjust Leading Character
if input_text.startswith("."):
    input_text = "dot" + input_text

# Step 4: Initialize Variables
counter = 0
char_list = []

# Step 5: Check for Leading "at"
if input_text.startswith("@"):
    input_text = "at" + input_text

# Step 6: Iterate Through Each Character
for char in input_text:
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
new_string = ''.join(char_list)

# Step 8: Adjust Trailing Character
if new_string.endswith("."):
    new_string = new_string[:-1] + "dot"

# Step 9: Output the Result
print(new_string)
