# Read a single line of input
input_string = input()  # Input is taken as a string

# Initialize variables
current_index = 0  # Index to track the position in the input
result_string = ''  # Result string starts empty

# Loop until the end of the input string
while current_index < len(input_string):  # Continue while there are more characters to process
    
    # Check for a '.' character
    if input_string[current_index] == '.':
        result_string += '0'  # Append '0' to the result string
        current_index += 1  # Move to the next character
        
    # Check for two consecutive character patterns
    elif (current_index + 1 < len(input_string)) and (input_string[current_index + 1] == '.'):
        result_string += '1'  # Append '1' to the result string
        current_index += 2  # Skip the next character
        
    else:
        result_string += '2'  # Append '2' to the result string
        current_index += 2  # Skip the next character

# Output the final result string
print(result_string)  # Print the constructed result string
