def process_input():
    # Read input from the standard input
    input_string = input().strip()

    # Replace 'dot' with '.' and 'at' with '@'
    input_string = input_string.replace('dot', '.').replace('at', '@')

    # If the first character is a '.', prepend 'dot'
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Initialize variables for processing
    count_at = 0
    result_array = []
    
    # If the first character is an '@', prepend 'at'
    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Iterate through each character in the modified input string
    for character in input_string:
        if character == '@':
            # Check if we have already added an '@'
            if count_at > 0:
                result_array.append('at')
            else:
                result_array.append('@')
                count_at = 1
        else:
            # Add non-@ character to result_array
            result_array.append(character)

    # Join the result_array into a single string
    final_string = ''.join(result_array)

    # If the last character is a '.', replace it with 'dot'
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'

    # Output the final processed string
    print(final_string)

# Call the function to execute the processing
process_input()
