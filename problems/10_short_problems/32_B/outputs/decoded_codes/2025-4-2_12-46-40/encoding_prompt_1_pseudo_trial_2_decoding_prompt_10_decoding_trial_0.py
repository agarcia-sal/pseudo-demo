def process_input_string():
    # Read input from the user
    input_string = input().strip()  # Remove leading and trailing whitespace

    # Initialize an index to track the current position within the string
    index = 0

    # Initialize an empty string to build the resulting output
    output_string = ''

    # Loop while the current index is less than the length of the input string
    while index < len(input_string):
        # Check if the current character is a dot
        if input_string[index] == '.':
            output_string += '0'  # Append '0' to output_string
            index += 1  # Move to the next character

        # Check if the next character is a dot (only if the current character was not a dot)
        elif index + 1 < len(input_string) and input_string[index + 1] == '.':
            output_string += '1'  # Append '1' to output_string
            index += 2  # Skip the next character

        # If not a dot nor a double dot, it must be '00'
        else:
            output_string += '2'  # Append '2' to output_string
            index += 2  # Skip the next character

    # Output the final result
    print(output_string)

# Call the function to execute the process
process_input_string()
