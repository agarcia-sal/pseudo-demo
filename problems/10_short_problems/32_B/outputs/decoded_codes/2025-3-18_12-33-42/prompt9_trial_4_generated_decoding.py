# Receive input from the user and remove any surrounding whitespace
input_string = input().strip()

# Initialize index and result
current_index = 0
numeric_output = ""

# Process the input string
while current_index < len(input_string):
    if input_string[current_index] == '.':
        numeric_output += '0'  # If current character is '.', append '0'
        current_index += 1      # Move to next character
    elif current_index + 1 < len(input_string) and input_string[current_index + 1] == '.':
        numeric_output += '1'  # If next character is '.', append '1'
        current_index += 2      # Move past both characters
    else:
        numeric_output += '2'  # Otherwise, append '2'
        current_index += 2      # Move past both characters

# Output the result
print(numeric_output)
