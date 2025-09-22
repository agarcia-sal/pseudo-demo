def decode_string():
    # Accept a string of characters consisting of '.' and '-'
    input_string = input()
    
    # Initialize variables
    index = 0
    decoded_output = ""

    # Process the input string
    while index < len(input_string):
        if input_string[index] == '.':
            decoded_output += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            decoded_output += '1'
            index += 2
        else:  # It's a hyphen
            decoded_output += '2'
            index += 2

    # Output the result
    print(decoded_output)

# Function call to execute the decoding of the input string
decode_string()
