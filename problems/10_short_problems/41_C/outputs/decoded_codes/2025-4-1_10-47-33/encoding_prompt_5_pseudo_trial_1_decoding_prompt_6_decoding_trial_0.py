# Read input from the user
input_text = input().strip()  # Remove any leading or trailing whitespace

# Replace keywords with symbols
modified_text = input_text.replace("dot", ".").replace("at", "@")

# Check for leading dot and update string accordingly
if modified_text.startswith("."):
    modified_text = "dot" + modified_text

# Initialize variables
counter_at_symbol = 0  # Counter for '@' appearances
processed_characters = []  # List to store processed characters
unused_variable = 0  # Unused as per original logic

# Fix the leading at
if modified_text.startswith("@"):
    modified_text = "at" + modified_text

# Process each character in the modified string
for char in modified_text:
    if char == "@":
        if counter_at_symbol > 0:  # Check if we've already encountered an '@'
            processed_characters.append("at")
            counter_at_symbol = 1  # Reset counter
        else:
            processed_characters.append("@")
            counter_at_symbol = 1  # Set counter to indicate we've seen an '@'
    else:
        processed_characters.append(char)  # Append the character as is

# Combine the characters into a single string
final_string = ''.join(processed_characters)

# Adjust trailing dot if necessary
if final_string.endswith("."):
    final_string = final_string[:-1] + "dot"  # Replace trailing '.' with 'dot'

# Output the final modified string
print(final_string)
