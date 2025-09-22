# Step 1: Read input from the user
input_string = input()

# Step 2: Replace keywords
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 3: Handle special case for initial character
if input_string.startswith("."):
    input_string = "dot" + input_string[1:]

# Step 4: Initialize variables
at_count = 0  # Counter for occurrences of "@"
result_list = []  # Results list to collect characters

# Step 5: Handle special case for email format
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]

# Step 6: Process each character
for current_char in input_string:
    if current_char == "@":
        if at_count > 0:  # Another "@" encountered
            result_list.append("at")  # Append "at"
            at_count = 1  # Set count to 1
        else:  # First occurrence of "@"
            result_list.append("@")  # Append "@"
            at_count = 1  # Set count to 1
    else:
        result_list.append(current_char)  # Append the current character

# Step 7: Combine results
output_string = ''.join(result_list)  # Join all elements to form a single string

# Step 8: Handle ending special case
if output_string.endswith("."):
    output_string = output_string[:-1] + "dot"  # Replace last character with "dot"

# Step 9: Output result
print(output_string)  # Print the final output string
