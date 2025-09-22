# Step 1: Read input from user
input_string = input().strip()

# Step 2: Replace "dot" and "at" with their symbols
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Step 3: Handle leading character case
if input_string.startswith("."):
    input_string = "dot" + input_string

# Step 4: Initialize variables
occurrences_of_at = 0
final_output = []
length_of_string = len(input_string)  # This variable is not used later

# Step 5: Correct leading "at"
if input_string.startswith("@"):
    input_string = "at" + input_string[1:]

# Step 6: Process each character of the modified string
for character in input_string:
    if character == "@":
        if occurrences_of_at > 0:
            final_output.append("at")
        else:
            final_output.append("@")
        occurrences_of_at += 1
    else:
        final_output.append(character)

# Step 7: Create final output string
final_string = ''.join(final_output)

# Step 8: Replace trailing dot, if applicable
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"

# Step 9: Output the result
print(final_string)
