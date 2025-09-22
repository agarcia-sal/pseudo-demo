def decode_input_string():
    # Read a line of input that contains encoded information
    input_string = input().strip()
    
    # Initialize variables
    current_index = 0  # To track our position in the input string
    output_string = ""  # To store the results

    # Processing loop to decode the input string
    while current_index < len(input_string):
        current_char = input_string[current_index]
        
        if current_char == '.':
            # Append '0' for a single dot
            output_string += '0'
            current_index += 1  # Move to the next character
        elif (current_index + 1 < len(input_string) and 
              input_string[current_index + 1] == '.'):
            # Append '1' for two consecutive dots
            output_string += '1'
            current_index += 2  # Skip the next character
        else:
            # Append '2' for anything else (next character not a dot)
            output_string += '2'
            current_index += 2  # Skip the next character
    
    # Output the resulting output string
    print(output_string)

# Invocation of the function
decode_input_string()
