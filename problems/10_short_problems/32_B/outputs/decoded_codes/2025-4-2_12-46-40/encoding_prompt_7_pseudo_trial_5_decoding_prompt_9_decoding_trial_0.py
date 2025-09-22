def convert_input_to_binary_string():
    # Read input string from standard input
    input_string = input()
    index = 0
    result_string = ""

    # Process each character in the input string
    while index < len(input_string):
        if input_string[index] == '.':
            # If current character is '.', append '0'
            result_string += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # If the next character is also '.', append '1'
            result_string += '1'
            index += 2
        else:
            # If the character is neither of the above, treat it as '2'
            result_string += '2'
            index += 2

    # Output the result string
    print(result_string)
