def process_input():
    # Read input from stdin and remove leading/trailing whitespaces
    input_string = input().strip()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    input_string = input_string.replace('dot', '.')
    input_string = input_string.replace('at', '@')

    # Check if the first character is a period ('.')
    if input_string and input_string[0] == '.':
        input_string = 'dot' + input_string[1:]

    # Initialize a counter and an empty list for constructing output
    counter = 0
    output_list = []

    # Check if the first character is '@', then modify it
    if input_string and input_string[0] == '@':
        input_string = 'at' + input_string[1:]

    # Loop through each character in the modified input_string
    for character in input_string:
        if character == '@':
            # Check if '@' has occurred previously
            if counter > 0:
                output_list.append('at')
            else:
                output_list.append('@')
            counter = 1
        else:
            output_list.append(character)
            counter = 0  # Reset counter for non-@ characters

    # Join the list of characters to form the final output string
    final_output_string = ''.join(output_list)

    # Check if the last character of the final output_string is a period ('.')
    if final_output_string and final_output_string[-1] == '.':
        final_output_string = final_output_string[:-1] + 'dot'

    # Print the final output string
    print(final_output_string)

# Call the function to execute the process
process_input()
