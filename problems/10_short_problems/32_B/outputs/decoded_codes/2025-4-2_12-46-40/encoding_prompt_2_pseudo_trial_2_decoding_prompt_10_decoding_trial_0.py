def decode_encoded_string():
    # Read a line of input that contains the encoded string
    encoded_string = input()
    
    # Initialize variables
    current_index = 0
    output_string = ""
    
    # Process the encoded string
    while current_index < len(encoded_string):
        current_char = encoded_string[current_index]
        
        if current_char == '.':
            # If the current character is a dot, append '0' to the output string
            output_string += '0'
            current_index += 1  # Move to the next character
            
        elif (current_index + 1 < len(encoded_string) and 
              encoded_string[current_index + 1] == '.'):
            # If the next character is also a dot, append '1' to the output string
            output_string += '1'
            current_index += 2  # Skip the next character
            
        else:
            # If the next character is not a dot, append '2' to the output string
            output_string += '2'
            current_index += 2  # Skip the next character

    # Output the resulting output string
    print(output_string)

# Run the function to decode the input string
decode_encoded_string()
