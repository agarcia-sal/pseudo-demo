def convert_input_to_output():
    # Read user input and strip unnecessary spaces
    input_string = input().strip()
    index = 0
    result_string = ""
    
    # Loop through the input string until the end is reached
    while index < len(input_string):
        # Check if the current character is a dot
        if input_string[index] == '.':
            result_string += '0'
            index += 1
        else:
            # Check the next character after the current one
            if index + 1 < len(input_string) and input_string[index + 1] == '.':
                result_string += '1'
                index += 2
            else:
                result_string += '2'
                index += 2

    # Output the resulting string
    print(result_string)

# Call the function to execute the program
convert_input_to_output()
