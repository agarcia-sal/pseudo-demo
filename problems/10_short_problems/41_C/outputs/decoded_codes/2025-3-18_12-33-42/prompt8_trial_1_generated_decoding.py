# Begin Program

# Read Input
input_email = input().strip()

# Replace Specific Words
input_email = input_email.replace("dot", ".").replace("at", "@")

# Check for Leading Character
if input_email.startswith('.'):
    input_email = 'dot' + input_email[1:]

# Initialize Variables
last_at_count = 0
processed_chars = []

# Check for Leading Character '@'
if input_email.startswith('@'):
    input_email = 'at' + input_email[1:]

# Process Each Character in the String
for char in input_email:
    if char == '@':
        if last_at_count > 0:
            processed_chars.append('at')
        else:
            processed_chars.append('@')
        last_at_count += 1
    else:
        processed_chars.append(char)

# Join the List into a String
final_email = ''.join(processed_chars)

# Check for Trailing Character
if final_email.endswith('.'):
    final_email = final_email[:-1] + 'dot'

# Output Result
print(final_email)

# End Program
