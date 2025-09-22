def process_input_string(input_string):
    # Initialize variables
    current_index = 0
    result_string = ""

    # Loop until the end of the input string
    while current_index < len(input_string):
        # Check for a '.' character
        if input_string[current_index] == '.':
            # Append '0' to the result string
            result_string += '0'
            # Move to the next character
            current_index += 1
        # Check for two consecutive character patterns
        elif (current_index + 1 < len(input_string)) and (input_string[current_index + 1] == '.'):
            # Append '1' to the result string
            result_string += '1'
            # Skip the next character
            current_index += 2
        else:
            # Append '2' to the result string
            result_string += '2'
            # Skip the next character
            current_index += 2

    # Output the final result string
    print(result_string)

# Read a single line of input
input_string = input()
process_input_string(input_string)
