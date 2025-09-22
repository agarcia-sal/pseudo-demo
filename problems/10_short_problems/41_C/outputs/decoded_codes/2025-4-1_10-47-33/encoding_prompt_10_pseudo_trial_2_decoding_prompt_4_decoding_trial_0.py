# Read Input
input_string = input().strip()  # Remove leading and trailing whitespace

# Replace Substrings
input_string = input_string.replace("dot", ".")
input_string = input_string.replace("at", "@")

# Check Starting Character
if input_string.startswith('.'):
    input_string = "dot" + input_string[1:]  # Prepend "dot" without the first character

# Initialize Variables
count_at = 0
result_list = []

# Handle Starting Character for `@`
if input_string.startswith('@'):
    input_string = "at" + input_string[1:]  # Prepend "at" without the first character

# Process Each Character
for character in input_string:
    if character == '@':
        if count_at > 0:
            result_list.append("at")
            count_at = 1  # Reset count for consecutive '@'
        else:
            result_list.append('@')
            count_at = 1
    else:
        result_list.append(character)  # Append other characters directly

# Join Result
processed_string = ''.join(result_list)

# Check Ending Character
if processed_string.endswith('.'):
    processed_string = processed_string[:-1] + "dot"  # Replace the last character with "dot"

# Output the Result
print(processed_string)
