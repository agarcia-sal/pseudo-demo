# Start of the email formatting program
# Step 1: Read input from user
input_string = input().strip()  # Read input and trim leading/trailing spaces

# Step 2: Replace "dot" and "at" with their symbols
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 3: Handle leading character case
if input_string.startswith("."):
    input_string = "dot" + input_string  # Prepend "dot" if starts with '.'

# Step 4: Initialize variables
occurrences_of_at = 0  # Counter for occurrences of "@"
final_output = []  # List to build the final output string

# Step 5: Correct leading "at"
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]  # Replace leading '@' with 'at'

# Step 6: Process each character of the modified string
for character in input_string:
    if character == "@":  # Check if character is '@'
        if occurrences_of_at > 0:  # If this is not the first '@'
            final_output.append("at")  # Append "at" if there's already an '@'
            occurrences_of_at = 1  # Mark that we've seen '@' again
        else:
            final_output.append("@")  # Append "@" if it's the first occurrence
            occurrences_of_at = 1  # Mark occurrence of the first '@'
    else:
        final_output.append(character)  # Append character as is

# Step 7: Create final output string
final_string = ''.join(final_output)  # Join the list into a single string

# Step 8: Replace trailing dot, if applicable
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Replace last character with "dot"

# Step 9: Output the result
print(final_string)  # Print the final modified string
