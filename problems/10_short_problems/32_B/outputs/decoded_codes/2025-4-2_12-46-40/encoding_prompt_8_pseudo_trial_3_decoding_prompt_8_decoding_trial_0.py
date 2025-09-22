# Define Input Source
input_str = input().strip()

# Initialize Variables
current_position = 0
result = ""

# Process the Input String
while current_position < len(input_str):
    if input_str[current_position] == '.':
        result += '0'
        current_position += 1
    elif current_position + 1 < len(input_str) and input_str[current_position + 1] == '.':
        result += '1'
        current_position += 2
    else:
        result += '2'
        current_position += 2

# Output the Result
print(result)
