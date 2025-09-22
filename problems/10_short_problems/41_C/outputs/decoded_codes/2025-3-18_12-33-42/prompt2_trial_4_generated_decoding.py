# Step 1: Read the input from the user and trim spaces
input_string = input().strip()

# Step 2: Replace "dot" with "."
formatted_string = input_string.replace("dot", ".")

# Step 3: Replace "at" with "@"
formatted_string = formatted_string.replace("at", "@")

# Step 4: Check if the string starts with "."
if formatted_string.startswith("."):
    formatted_string = "dot" + formatted_string[1:]

# Step 5: Initialize counter and output list
counter = 0
output_list = []

# Step 6: Initialize current length (not utilized further)
current_length = len(formatted_string)

# Step 7: Check if the string starts with "@"
if formatted_string.startswith("@"):
    formatted_string = "at" + formatted_string[1:]

# Step 8: Iterate over each character in the formatted string
for char in formatted_string:
    if char == "@":
        if counter == 1:  # If it's not the first occurrence
            output_list.append("at")
        else:  # It's the first occurrence
            output_list.append("@")
            counter = 1  # Mark that we counted a "@"
    else:
        output_list.append(char)

# Step 9: Join the list into a final string
final_string = ''.join(output_list)

# Step 10: Check if the last character is "."
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Step 11: Output the final formatted string
print(final_string)
