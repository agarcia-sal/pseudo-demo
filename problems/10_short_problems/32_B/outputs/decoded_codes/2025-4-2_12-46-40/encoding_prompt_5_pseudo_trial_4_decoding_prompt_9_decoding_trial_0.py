# Accept a string of characters from the user
input_string = input()

# Initialize index counter and output variable
i = 0
decoded_output = ""

# Process the input string
while i < len(input_string):
    if input_string[i] == '.':
        # Append '0' for a single dot
        decoded_output += '0'
        i += 1  # Move to the next character
    elif i + 1 < len(input_string) and input_string[i + 1] == '.':
        # Append '1' for two consecutive dots
        decoded_output += '1'
        i += 2  # Skip to the character after the next
    else:
        # Append '2' for a hyphen or other case
        decoded_output += '2'
        i += 2  # Skip to the character after the next

# Output the final decoded result
print(decoded_output)
