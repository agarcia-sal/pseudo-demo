# Read input from the user and strip surrounding whitespace
email_string = input().strip()

# Replace 'dot' with '.' and 'at' with '@'
email_string = email_string.replace("dot", ".")
email_string = email_string.replace("at", "@")

# Handle leading period
if email_string.startswith('.'):
    email_string = 'dot' + email_string[1:]

# Handle leading at symbol
if email_string.startswith('@'):
    email_string = 'at' + email_string[1:]

# Prepare for conversion
counter = 0
formatted_characters = []

# Process each character in the email string
for character in email_string:
    if character == '@':
        if counter > 0:
            formatted_characters.append("at")
            counter = 1
        else:
            formatted_characters.append("@")
            counter = 1
    else:
        formatted_characters.append(character)

# Join characters into a single string
final_string = ''.join(formatted_characters)

# Handle trailing period
if final_string.endswith('.'):
    final_string = final_string[:-1] + 'dot'

# Output the formatted email-like string
print(final_string)
