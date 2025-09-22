# Read input and remove any leading or trailing whitespace
input_string = input().strip()

# Initialize position for processing the string
current_position = 0
# Initialize the result string to store numerical representation
result = ""

# Process the input string while there are characters left to analyze
while current_position < len(input_string):
    if input_string[current_position] == '.':
        # If the current character is a dot, append '0' to result
        result += '0'
        current_position += 1  # Move to the next character
    elif (current_position + 1 < len(input_string) and 
          input_string[current_position + 1] == '.'):
        # If the next character is also a dot, append '1' to result
        result += '1'
        current_position += 2  # Move ahead by 2 positions
    else:
        # If it's any other character or single dot not followed by another dot, append '2' to result
        result += '2'
        current_position += 2  # Move ahead by 2 positions

# Output the final result string
print(result)
