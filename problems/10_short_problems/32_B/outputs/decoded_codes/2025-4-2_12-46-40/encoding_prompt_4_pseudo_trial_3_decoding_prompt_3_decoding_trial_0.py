def transform_input_string():
    # Read a line of input and remove any whitespace
    input_string = input().strip()

    # Initialize index and result string
    index = 0
    result = ""

    # Loop until the end of the input string is reached
    while index < len(input_string):
        # Check if the current character is a single dot
        if input_string[index] == '.':
            result += '0'
            index += 1
        else:
            # Check the next character to determine the value to append
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                result += '1'
                index += 2
            else:
                result += '2'
                index += 2

    # Output the final result
    print(result)

# Call the function to execute
transform_input_string()
