def translate_encoding():
    # Read input and strip any extra spaces or newlines
    encoded_string = input().strip()

    # Initialize variables
    current_position = 0
    result = ""

    # Process the input
    while current_position < len(encoded_string):
        # Check the character at the current position
        if encoded_string[current_position] == '.':
            result += '0'  # A single dot represents 0
            current_position += 1
        else:
            # Check the next character for pairs of dots or a dash
            if (current_position + 1 < len(encoded_string) and
                    encoded_string[current_position + 1] == '.'):
                result += '1'  # A pair of dots represents 1
                current_position += 2
            else:
                result += '2'  # A sequence starting with a dash represents 2
                current_position += 2

    # Output the result
    print(result)

# Example function call
translate_encoding()
