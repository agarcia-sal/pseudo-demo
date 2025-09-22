def decode_input():
    # Read input data from standard input and strip any extra whitespace
    input_string = input().strip()
    index = 0
    result_string = ""

    # Process the input string until the end is reached
    while index < len(input_string):
        if input_string[index] == '.':
            # If the current character is a '.', append '0' to result
            result_string += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # If the next character is also '.', append '1' to result
            result_string += '1'
            index += 2
        else:
            # Otherwise, append '2' to result
            result_string += '2'
            index += 2

    # Output the resulting string
    print(result_string)
