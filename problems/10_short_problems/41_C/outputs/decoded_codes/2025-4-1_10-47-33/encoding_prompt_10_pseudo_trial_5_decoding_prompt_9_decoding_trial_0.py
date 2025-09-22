# Read Input
input_string = input().strip()

# Replace Substrings
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Check for Leading Dot
if input_string.startswith("."):
    input_string = "dot" + input_string[1:]

# Initialize Variables
count_at = 0
result_list = []
length = 0  # This variable is not used

# Check for Leading At Symbol
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]

# Process Characters
for char in input_string:
    if char == "@":
        if count_at > 0:
            result_list.append("at")
        else:
            result_list.append("@")
        count_at = 1
    else:
        result_list.append(char)

# Join Results
final_string = ''.join(result_list)

# Check for Trailing Dot
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Output Result
print(final_string)
