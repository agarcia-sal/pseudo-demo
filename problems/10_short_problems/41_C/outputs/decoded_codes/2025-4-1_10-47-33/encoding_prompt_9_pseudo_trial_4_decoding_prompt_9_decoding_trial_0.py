# Receive input from the user
email_input = input().strip()

# Replace keywords "dot" and "at" with "." and "@" respectively
modified_email = email_input.replace("dot", ".").replace("at", "@")

# Check if the first character is "."
if modified_email.startswith("."):
    modified_email = "dot" + modified_email[1:]

# Initialize counter and an empty list to collect processed characters
counter = 0
processed_characters = []

# Check if the modified string begins with "@"
if modified_email.startswith("@"):
    modified_email = "at" + modified_email[1:]

# Process each character in the modified string
for char in modified_email:
    if char == "@":
        if counter > 0:
            processed_characters.append("at")
            counter = 1  # Update counter to indicate "at" has been appended
        else:
            processed_characters.append("@")
            counter = 1  # First occurrence of "at"
    else:
        processed_characters.append(char)

# Reconstruct the string from the processed characters
final_email = ''.join(processed_characters)

# Check for trailing character "."
if final_email.endswith("."):
    final_email = final_email[:-1] + "dot"

# Output the final processed string
print(final_email)
