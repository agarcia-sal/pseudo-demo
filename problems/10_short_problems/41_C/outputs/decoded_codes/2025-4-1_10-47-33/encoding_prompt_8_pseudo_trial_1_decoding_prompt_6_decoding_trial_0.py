# Step 1: Read input from the user
input_string = input().strip()  # Remove leading and trailing whitespace

# Step 2: Replace terms with corresponding symbols
modified_string = input_string.replace("dot", ".").replace("at", "@")

# Step 3: Handle leading character
if modified_string.startswith("."):
    modified_string = "dot" + modified_string[1:]  # Remove leading "." and prepend "dot"

# Step 4: Initialize variables
count_at = 0  # To track the number of "@" symbols processed
output_list = []  # To build the final output

# Step 5: Check leading character for "at"
if modified_string.startswith("@"):
    modified_string = "at" + modified_string[1:]  # Change first "@" to "at"

# Step 6: Process each character
for char in modified_string:
    if char == "@":
        if count_at > 0:
            output_list.append("at")  # Replace subsequent "@" with "at"
        else:
            output_list.append("@")  # Keep the first "@"
            count_at = 1  # Increment count
    else:
        output_list.append(char)  # Append other characters

# Step 7: Join and finalize output
final_string = ''.join(output_list)  # Join list into a string

# Ensure the last character is not invalid
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Replace the last "." with "dot"

# Step 8: Print output
print(final_string)
