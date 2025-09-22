def translate_encoding():
    # Read input
    encoded_string = input().strip()
    
    # Initialize variables
    current_position = 0
    result = ''

    # Process the input
    while current_position < len(encoded_string):
        if encoded_string[current_position] == '.':
            # A single dot represents 0
            result += '0'
            current_position += 1
        else:
            # Check the next character
            if (current_position + 1 < len(encoded_string) and 
                encoded_string[current_position + 1] == '.'):
                # A pair of dots represents 1
                result += '1'
                current_position += 2
            else:
                # A sequence starting with a dash represents 2
                result += '2'
                current_position += 2

    # Output the result
    print(result)

# Call the function to run the program
translate_encoding()
