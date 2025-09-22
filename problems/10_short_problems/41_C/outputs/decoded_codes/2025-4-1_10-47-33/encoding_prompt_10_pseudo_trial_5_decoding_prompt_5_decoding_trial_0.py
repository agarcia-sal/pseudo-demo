# Read input from the user
input_string = input().strip()

# Replace substrings in the input_string
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Check for leading dot and prepend "dot" if necessary
if input_string.startswith("."):
    input_string = "dot" + input_string[1:]

# Initialize variables
count_at = 0
result_list = []

# Check for leading at symbol and prepend "at"
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]

# Process each character in the input_string
for char in input_string:
    if char == "@":  # Check for at symbol
        if count_at > 0:
            result_list.append("at")  # Append "at" if count_at > 0
        else:
            result_list.append("@")  # Append "@" for the first occurrence
        count_at = 1  # Set count_at to indicate we've seen an @
    else:
        result_list.append(char)  # Append the current character

# Join the result list into a single string
final_string = ''.join(result_list)

# Check for trailing dot and adjust final_string if necessary
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Output the final string
print(final_string)
