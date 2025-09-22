# This program converts a string of characters into a numerical string based on specified rules.

# Read input, removing any surrounding whitespace
input_string = input().strip()

# Initialize position index and result string
current_index = 0
result_string = ""

# Loop through the input string until the end is reached
while current_index < len(input_string):
    # Check the character at the current index
    if input_string[current_index] == '.':
        # If current character is a dot, append '0' to result
        result_string += '0'
        
        # Move to the next character
        current_index += 1
        
    elif (current_index + 1) < len(input_string and input_string[current_index + 1] == '.'):
        # If the next character is a dot, append '1' to result
        result_string += '1'
        
        # Move the index ahead by two characters
        current_index += 2
        
    else:
        # Append '2' to the result as neither of the above conditions were met
        result_string += '2'
        
        # Move the index ahead by two characters
        current_index += 2

# Output the final result string
print(result_string)

# Test cases (examples):
# For input "....", the output will be "0000".
# For input "..", the output will be "1".
# For input "....a..", the output will be "0002" since the 'a' changes how we evaluate the string.
