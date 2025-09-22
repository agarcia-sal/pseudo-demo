# Function to decode a string of encoded information
def decode_string():
    # Read input string
    input_string = input()
    
    # Initialize current index and output string
    current_index = 0
    output_string = ""
    
    # Processing loop to iterate through the string
    while current_index < len(input_string):
        # Check the current character
        if input_string[current_index] == '.':
            output_string += '0'  # Append '0' for a single dot
            current_index += 1  # Move to the next character
        elif (current_index + 1 < len(input_string) and 
              input_string[current_index + 1] == '.'):
            output_string += '1'  # Append '1' for two consecutive dots
            current_index += 2  # Skip the next character
        else:
            output_string += '2'  # Append '2' for any other character
            current_index += 2  # Skip the next character
    
    # Output the resulting decoded string
    print(output_string)

# Example test case
# Assuming the input will be provided by the user so we will not execute here.
