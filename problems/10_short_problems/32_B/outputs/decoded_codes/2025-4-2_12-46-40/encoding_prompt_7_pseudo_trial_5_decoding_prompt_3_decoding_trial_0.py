def convert_input_to_binary_string():
    # Read string input from standard input
    input_string = input()
    index = 0
    result_string = ""

    # Process the input string until we've checked all characters
    while index < len(input_string):
        # Check for '.' character
        if input_string[index] == '.':
            result_string += '0'
            index += 1
        # Check for patterns of two '.' characters
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            result_string += '1'
            index += 2
        else:
            # Handle other cases (if it is not a single '.' or '.')
            result_string += '2'
            index += 2

    # Output the result string
    print(result_string)

# Optional: You could run a test like this
# convert_input_to_binary_string()
