# Step 1: Read input from user
input_string = input().strip()  # Read user input and remove any leading/trailing spaces

# Step 2: Replace "dot" and "at" with their symbols
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 3: Handle leading character case
if input_string.startswith("."):
    input_string = "dot" + input_string  # Prepend "dot" if the string starts with a "."

# Step 4: Initialize variables
occurrences_of_at = 0  # Counter for occurrences of "@"
final_output = []  # List to build the final output string

# Step 5: Correct leading "at"
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]  # Replace leading "@" with "at" + rest of the string

# Step 6: Process each character of the modified string
for character in input_string:
    if character == "@":  # Check if the character is "@"
        if occurrences_of_at > 0:
            final_output.append("at")  # Append "at" if "@" has been seen before
            occurrences_of_at = 1  # Update occurrences of "@"
        else:
            final_output.append("@")  # Append "@" for the first occurrence
            occurrences_of_at = 1  # Update occurrences of "@"
    else:
        final_output.append(character)  # Append any other character as is

# Step 7: Create final output string
final_string = ''.join(final_output)  # Join all elements in final_output into a single string

# Step 8: Replace trailing dot, if applicable
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Replace trailing "." with "dot"

# Step 9: Output the result
print(final_string)  # Print the final modified string
