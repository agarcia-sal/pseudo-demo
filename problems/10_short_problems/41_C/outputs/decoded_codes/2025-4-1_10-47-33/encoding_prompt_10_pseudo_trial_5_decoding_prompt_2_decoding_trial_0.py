# Step 1: Read Input
input_string = input().strip()

# Step 2: Replace Substrings
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 3: Check for Leading Dot
if input_string.startswith("."):
    input_string = "dot" + input_string[1:]

# Step 4: Initialize Variables
count_at = 0
result_list = []
length = 0  # length is defined but not used

# Step 5: Check for Leading At Symbol
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]

# Step 6: Process Characters
for char in input_string:
    if char == "@":
        if count_at > 0:
            result_list.append("at")
        else:
            result_list.append("@")
        count_at = 1
    else:
        result_list.append(char)

# Step 7: Join Results
final_string = ''.join(result_list)

# Step 8: Check for Trailing Dot
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Step 9: Output Result
print(final_string)
