# Read input and clean it of any leading or trailing whitespace
email_input = input().strip()

# Replace occurrences of "dot" with '.' and "at" with '@'
email_input = email_input.replace("dot", ".").replace("at", "@")

# Ensure the email does not start with '.' by prepending "dot" if needed
if email_input.startswith('.'):
    email_input = "dot" + email_input

# Initialize state variables
previous_at_count = 0
output_characters = []

# Handle the '@' character
if email_input.startswith('@'):
    email_input = "at" + email_input[1:]

# Process each character in the cleaned string
for current_character in email_input:
    if current_character == '@':
        if previous_at_count > 0:
            output_characters.append("at")
            previous_at_count = 1
        else:
            output_characters.append('@')
            previous_at_count = 1
    else:
        output_characters.append(current_character)

# Form the final output string
final_output = ''.join(output_characters)

# Replace the last character with "dot" if it is a '.' 
if final_output.endswith('.'):
    final_output = final_output[:-1] + "dot"

# Display the result
print(final_output)
