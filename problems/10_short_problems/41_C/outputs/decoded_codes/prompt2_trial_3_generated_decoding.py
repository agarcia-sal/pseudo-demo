# Step 1: Read Input
input_string = input().strip()

# Step 2: Replace Text
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Check for Leading Dot
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]

# Step 4: Initialization
at_counter = 0
result_characters = []
length = 0  # unused variable

# Step 5: Check for Leading At
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]

# Step 6: Process Each Character in the Modified String
for char in modified_string:
    if char == "@":
        if at_counter > 0:
            result_characters.append("at")
            at_counter = 1
        else:
            result_characters.append("@")
            at_counter = 1
    else:
        result_characters.append(char)
        at_counter = 0  # reset since we're not at '@'

# Step 7: Combine Characters
final_output = ''.join(result_characters)

# Step 8: Check for Trailing Dot
if final_output.endswith("."):
    final_output = final_output[:-1] + "dot"

# Step 9: Output Result
print(final_output)
