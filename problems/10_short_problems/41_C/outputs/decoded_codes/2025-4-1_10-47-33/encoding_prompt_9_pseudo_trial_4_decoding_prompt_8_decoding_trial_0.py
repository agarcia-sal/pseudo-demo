# Step 1: Receive Input
input_string = input().strip()

# Step 2: Replace Keywords
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Check Leading Character
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]

# Step 4: Initialize the List and Counter
counter = 0
result_list = []

# Step 5: Check for Leading "at"
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]

# Step 6: Process Each Character
for char in modified_string:
    if char == "@":
        if counter > 0:
            result_list.append("at")
            counter = 1
        else:
            result_list.append(char)
            counter = 1
    else:
        result_list.append(char)

# Step 7: Reconstruct the String
final_string = ''.join(result_list)

# Step 8: Check for Trailing Character
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Step 9: Output the Result
print(final_string)
