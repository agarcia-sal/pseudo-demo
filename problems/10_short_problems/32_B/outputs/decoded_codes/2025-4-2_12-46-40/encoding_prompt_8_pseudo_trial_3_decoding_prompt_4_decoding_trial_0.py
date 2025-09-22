# Read input string from standard input and trim whitespace
input_string = input().strip()

# Initialize the current position and the result string
current_position = 0
result = ""

# Process the input string
while current_position < len(input_string):
    if input_string[current_position] == '.':
        # Add '0' for a single dot
        result += '0'
        current_position += 1
    elif (current_position + 1) < len(input_string) and input_string[current_position + 1] == '.':
        # Add '1' for a pair of dots
        result += '1'
        current_position += 2  # Move ahead by 2 positions
    else:
        # Add '2' for any other configuration
        result += '2'
        current_position += 2  # Move ahead by 2 positions

# Output the final result string
print(result)
