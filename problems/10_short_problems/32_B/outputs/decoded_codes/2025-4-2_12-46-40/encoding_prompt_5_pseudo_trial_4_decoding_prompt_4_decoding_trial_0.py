def decode_sequence():
    # Accept a string of characters from the user
    input_string = input()
    
    # Initialize variables
    i = 0
    decoded_output = ""

    # Process input string
    while i < len(input_string):
        if input_string[i] == '.':
            decoded_output += '0'  # Append '0' for a single dot
            i += 1  # Move to the next character
        elif i + 1 < len(input_string) and input_string[i + 1] == '.':
            decoded_output += '1'  # Append '1' for two consecutive dots
            i += 2  # Skip to character after next
        else:  # The only case left is a hyphen
            decoded_output += '2'  # Append '2' for a hyphen
            i += 2  # Skip to character after next

    # Output result
    print(decoded_output)

# Call the function to execute the decoding
decode_sequence()
