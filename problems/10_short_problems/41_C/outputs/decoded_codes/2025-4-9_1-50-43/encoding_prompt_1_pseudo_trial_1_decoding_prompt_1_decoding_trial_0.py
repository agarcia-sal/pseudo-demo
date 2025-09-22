# Step 1: Define Input
email_input = input().strip()

# Step 2: Replace Text Patterns
email_input = email_input.replace("dot", ".").replace("at", "@")

# Step 3: Handle Leading Characters
if email_input.startswith("."):
    email_input = "dot" + email_input

# Step 4: Initialize Variables
occurrences = 0
formatted_characters = []

# Step 5: Handle Leading "@" Character
if email_input.startswith("@"):
    email_input = "at" + email_input

# Step 6: Iterate Through Each Character in the Input
for character in email_input:
    if character == "@":
        if occurrences > 0:
            formatted_characters.append("at")
            occurrences = 1
        else:
            formatted_characters.append("@")
            occurrences = 1
    else:
        formatted_characters.append(character)

# Step 7: Join Characters
final_email = ''.join(formatted_characters)

# Step 8: Handle Trailing Characters
if final_email.endswith("."):
    final_email = final_email[:-1] + "dot"

# Step 9: Output the Result
print(final_email)
