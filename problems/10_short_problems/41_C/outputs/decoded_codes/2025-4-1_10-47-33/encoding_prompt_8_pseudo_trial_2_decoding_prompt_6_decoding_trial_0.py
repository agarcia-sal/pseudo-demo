# Step 1: Read Input
email_string = input().strip()  # Get input line and remove surrounding whitespace

# Step 2: Replace Keywords
email_string = email_string.replace("dot", ".")  # Replace 'dot' with '.'
email_string = email_string.replace("at", "@")    # Replace 'at' with '@'

# Step 3: Handle Leading Period
if email_string.startswith('.'):
    email_string = 'dot' + email_string[1:]  # Change first character to 'dot'

# Step 4: Check for Leading At Symbol
if email_string.startswith('@'):
    email_string = 'at' + email_string[1:]  # Change first character to 'at'

# Step 5: Prepare for Conversion
counter = 0  # Initialize counter
formatted_characters = []  # List to store processed characters

# Step 6: Process Each Character
for character in email_string:
    if character == '@':
        if counter > 0:
            formatted_characters.append("at")  # Append 'at' if it's a subsequent '@'
            counter = 1  # Update counter
        else:
            formatted_characters.append("@")  # Append '@' for the first occurrence
            counter = 1  # Set counter
    else:
        formatted_characters.append(character)  # Append regular characters

# Step 7: Join Characters into a String
final_string = ''.join(formatted_characters)  # Combine all characters

# Step 8: Handle Trailing Period
if final_string.endswith('.'):
    final_string = final_string[:-1] + "dot"  # Replace trailing '.' with 'dot'

# Step 9: Output the Result
print(final_string)  # Print the formatted email-like string
