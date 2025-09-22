# Read input from the user
input_string = input().strip()  # Remove leading and trailing whitespace

# Replace "dot" with "." and "at" with "@" in the input string
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Check if the first character is a dot
if input_string.startswith("."):
    input_string = "dot" + input_string[1:]  # Prepend "dot" to input_string

# Initialize variables for tracking occurrences
count_at = 0  # Count for "at" occurrences
result_list = []  # List to store processed characters

# Check if the first character is an "at" symbol
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]  # Prepend "at" to input_string

# Process each character in the modified input_string
for char in input_string:
    if char == "@":  # Check for "at" symbol
        if count_at > 0:
            result_list.append("at")  # Append "at" if already counted once
        else:
            result_list.append("@")  # Append "@" as it is the first occurrence
        count_at = 1  # Set count_at to indicate we have found an "at"
    else:
        result_list.append(char)  # Append other characters as they are

# Join the processed characters into a single string
final_string = ''.join(result_list)

# Check if the final string ends with a dot and handle it
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Remove the trailing dot and append "dot"

# Output the result
print(final_string)
