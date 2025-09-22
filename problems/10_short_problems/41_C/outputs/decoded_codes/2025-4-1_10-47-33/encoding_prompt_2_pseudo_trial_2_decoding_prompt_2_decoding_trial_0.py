# Step 1: Receive Input
input_string = input().strip()

# Step 2: Replace Specific Strings
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 3: Check Beginning of String
if input_string and input_string[0] == ".":
    input_string = "dot" + input_string[1:]

# Step 4: Initialize Variables
at_counter = 0
collected_chars = []
char_index = 0

# Step 5: Handle Starting Character
if input_string and input_string[0] == "@":
    input_string = "at" + input_string[1:]

# Step 6: Iterate Through Characters
for char in input_string:
    if char == "@":
        if at_counter > 0:
            collected_chars.append("at")
        else:
            collected_chars.append("@")
        at_counter += 1
    else:
        collected_chars.append(char)

# Step 7: Combine Collected Characters
final_string = ''.join(collected_chars)

# Step 8: Final Adjustment
if final_string and final_string[-1] == ".":
    final_string = final_string[:-1] + "dot"

# Step 9: Output the Result
print(final_string)
