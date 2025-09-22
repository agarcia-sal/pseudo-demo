# Step 1: Read Input
email_input = input().strip()  # Obtain input from user and remove whitespace

# Step 2: Replace Substrings
email_input = email_input.replace("dot", ".")  # Replace 'dot' with '.'
email_input = email_input.replace("at", "@")    # Replace 'at' with '@'

# Step 3: Ensure Starting Character Rule
if email_input.startswith("."):
    email_input = "dot" + email_input  # Prepend 'dot' if the input starts with '.'

# Step 4: Initialize State Variables
previous_at_count = 0
output_characters = []  # List to hold processed characters

# Step 5: Handle '@' Character
if email_input.startswith("@"):
    email_input = "at" + email_input[1:]  # Replace first character with 'at'

# Step 6: Process Each Character in the String
for current_character in email_input:
    if current_character == "@":
        if previous_at_count > 0:
            output_characters.append("at")  # Append 'at' if '@' appears again
            previous_at_count = 1
        else:
            output_characters.append("@")  # Append '@' for the first occurrence
            previous_at_count = 1
    else:
        output_characters.append(current_character)  # Append normal characters

# Step 7: Form the Final Output String
final_output = ''.join(output_characters)  # Join all characters to form the final string
if final_output.endswith("."):
    final_output = final_output[:-1] + "dot"  # Replace last '.' with 'dot'

# Step 8: Display the Result
print(final_output)  # Output the final result
