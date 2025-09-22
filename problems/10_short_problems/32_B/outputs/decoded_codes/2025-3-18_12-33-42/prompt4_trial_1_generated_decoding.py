def transform_string():
    # Read input from standard input
    input_string = input()
    
    # Initialize index and output string
    index = 0
    output_string = ""

    # Loop through the input string until the end
    while index < len(input_string):
        # Check the current character
        if input_string[index] == '.':
            # Append '0' to the output_string
            output_string += '0'
            index += 1
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            # Append '1' to the output_string
            output_string += '1'
            index += 2
        else:
            # Append '2' to the output_string
            output_string += '2'
            index += 2

    # Print the final output string
    print(output_string)

# Call the function to execute the transformation
transform_string()
