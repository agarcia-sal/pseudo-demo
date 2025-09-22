def transform_string():
    # Read the input string from the user
    input_string = input()
    
    # Initialize variables
    index = 0
    output_string = ""

    # Loop through the input string until we reach the end
    while index < len(input_string):
        if input_string[index] == '.':
            # If current character is a '.', add '0' to output_string
            output_string += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # If next character is also '.', add '1' to output_string
            output_string += '1'
            index += 2
        else:
            # Otherwise, add '2' to output_string
            output_string += '2'
            index += 2

    # Output the result
    print(output_string)

# Call the function to execute the transformation
transform_string()
