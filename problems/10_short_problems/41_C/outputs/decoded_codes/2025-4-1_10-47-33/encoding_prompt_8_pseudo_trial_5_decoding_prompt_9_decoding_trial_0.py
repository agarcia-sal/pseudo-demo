# Begin the transformation script
# Step 1: Read input from user
input_string = input().strip()  # Read the input and trim spaces

# Step 2: Replace "dot" and "at" with their symbols
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 3: Handle leading character case
if input_string.startswith("."):
    input_string = "dot" + input_string  # Prepend "dot" if it starts with '.'

# Step 4: Initialize variables
occurrences_of_at = 0
final_output = []  # List to build the output
# length_of_string is not actively used further

# Step 5: Correct leading "at"
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]  # Replace leading '@' with "at"

# Step 6: Process each character of the modified string
for character in input_string:
    if character == "@":
        if occurrences_of_at > 0:
            final_output.append("at")  # Append "at" if it is not the first occurrence
        else:
            final_output.append("@")  # Append "@" directly for the first occurrence
            occurrences_of_at += 1
    else:
        final_output.append(character)  # Append the character as is

# Step 7: Create final output string
final_string = ''.join(final_output)  # Join all elements into a single string

# Step 8: Replace trailing dot, if applicable
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Replace last '.' with 'dot'

# Step 9: Output the result
print(final_string)  # Print the final modified string
